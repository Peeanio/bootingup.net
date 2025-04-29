---
layout: post
title: "Arch EFI Luks"
date: 2025-04-22 00:00:00 -0700
categories: Blog update
---

Setting up FDE with UKI (Unified Kernel Images) and Secure Boot with Arch Linux was slightly more confusing that I anticipated. Just wanted to knock out a quick how to on actually building this the right way. It seems to be the right configuration conceptually, but the tools used like `dracut` vs `mkinitcpio` in the wiki made it hard to piece together. A opinionated Ansible playbook is hopefully coming soon. 

1. Boot the system into the UEFI/BIOS. Set `Secure Boot` to `Setup` mode.
2. Boot into the live Arch ISO and perform typical setup steps from the installation guide.
    - Setup networking
    - `timedatectl` to sync clocks
3. Partition and encrypt the disks. This can be fairly arbitrary, but an unencrypted FAT32 partition for the UKI is required. I'll outline a sample partition scheme here:
    - `fdisk /dev/sda`: `g` for GPT, `n` for new partition, 1GB size (for EFI), `n` with remaining for LUKS, `w` to save
    - `mkfs.fat -F32 /dev/sda1` for the EFI filesystem
    - `cryptsetup luksFormat /dev/sda2`, enter the passphrase. It can be removed later, and we can store the key in the TPM
    - `cryptsetup open /dev/sda2 crypt` to decrypt and have the device writeable
    - `pvcreate /dev/mapper/crypt`, `vgcreate root /dev/mapper/crypt`, `lvcreate -l 100%FREE root root-lv`, `mkfs.ext4 /dev/mapper/root-root-lv` to create a root filesystem on the LUKS partition.
4. Mount the filesystems, root before EFI to ensure everything is written properly 
    - `mount /dev/mapper/root-root-lv /mnt`, `mount /dev/sda1 /mnt/efi --mkdir`
5. Pacstrap the system, with whatever packages you need on disk 
    - `pacstrap -K /mnt base linux linux-firmware vi sbctl efibootmgr`
6. Generate the fstab `genfstab -U /mnt >> /mnt/etc/fstab`
7. Chroot `arch-chroot /mnt`
8. Now that we're in the disk itself, there's a few tasks to take care of
    - `ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime`
    - Set locale in `/etc/locale.conf` and run `locale-gen`
    - Set the hostname in `/etc/hostname`
9. Use `efibootmgr` to remove any unneeded boot entries, like old Windows boot entries
    - `efibootmgr --unicode` to print, `efibootmgr --unicode --bootnum 0000 --delete-bootnum` to remove
10. Set your kernel cmdline parameters in `/etc/kernel/cmdline` and `/etc/kernel/cmdline_fallback`. These should at least include the UUID's of the root system.
    - ```rd.luks.uuid=<<luks uuid>>  root=UUID=<<ext4 lvm uuid>> rw ```
11. Edit `/etc/mkinintcpio.conf` to have the correct `HOOKS` line
    - ```HOOKS=(base systemd keyboard udev autodetect microcode modconf kms keymap consolefont sd-vconsole block sd-encrypt lvm2 filesystems fsck)```
12. Edit `/etc/mkinitcpio.d/linux.preset` to have `mkinitcpio generate the two kernel options with UKI
    - ```default_uki="/efi/EFI/Linux/arch-linux.efi" fallback_uki="/efi/EFI/Linux/arch-linux-fallback.efi" fallback_options="-S autodetect"```
13. Create the directories for the UKI's
    - `mkdir /efi/EFI/Linux`
14. Generate and install the Secure Boot keys. Install the Microsoft keys if required
    - `sbctl create-keys`
    - `sbctl enroll-keys -m`
15. Create a hook for `mkinitcpio` to sign the created keys
    - `/etc/initcpio/post/uki-sbsign`: '''
#!/usr/bin/env bash

uki="$3"
[[ -n "$uki" ]] || exit 0

keypairs=(/var/lib/sbctl/keys/db.key /var/lib/sbctl/keys/db.crt)

for (( i=0; i<${keypairs[@]}; i+=2 )); do
        key="${keypairs[$i]}" cert="${keypairs[(( i + 1 ))]}"
        if ! sbverify --cert "$cert" "$uki" &>/dev/null; then
                sbsign --key "$key" --cert "$cert" --output "$uki" "$uki"
        fi
done
'''
16. Create EFI boot entries for the UKI's:
    - `efibootmgr --create --disk /dev/sda1 --part 1 --label "Arch Linux" --loader '\EFI\Linux\arch-linux.efi' --unicode`
    - `efibootmgr --create --disk /dev/sda1 --part 1 --label "Arch Linux Fallback" --loader '\EFI\Linux\arch-linux-fallback.efi' --unicode`
17. If desired, create a luks key in the TPM
    - `systemd-cryptenroll --tpm2-device=auto --tpm2-pcrs=7 /dev/sda2`
18. Finish Arch install/user setup as required and reboot. On reboot, Secure Boot should be enabled and working, and the EFI should boot the kernel. Enjoy!
