Title: Chromebook as a Linux Ultrabook
Generator: org-pelican
Author: Nathan Mador-House
Author_Gravatar: http://www.gravatar.com/avatar/30ab82b51f4e3f7d703fd9f845a05b50
Date: 2016-12-01
Lang: en
Summary: Does it make sense to get a Chromebook primarily for use as a Linux ultrabook?
Status: published
Category: Consumer
Tags: Linux i3wm Laptops Chromebook


# Table of Contents

1.  [Which Linux Distro?](#orgaf16a32)
2.  [Priority of Needs](#org9c92781)
3.  [Dual Booting](#org804e391)
4.  [My Top Choices](#org2ec99e2)
5.  [What did I end up getting?](#org2801db6)



<a id="orgaf16a32"></a>

# Which Linux Distro?

First off it is important to understand that Chromebooks do not play nice with many distributions. If you are going to be using it as an Ultrabook, I would highly recommend the incredibly stable and optimized [GalliumOS](https://galliumos.org) as your distro. Not only does it work well out of the box with many Chromebook devices, the community is also quite helpful if you run into trouble.

That's not to say that you have unlimited options of distros when it comes to installing on Windows laptops either. There are a plethora of hardware compatibility traps to be wary of on the Windows side, but with enough research the likelihood is that you can find a compatible laptop for your distro of choice.


<a id="org9c92781"></a>

# Priority of Needs

Here was my personal priority:

1.  High quality screen (1080p, IPS, anti-glare, >=12.5")
2.  Performance (Intel Celeron/Core)
3.  Lightweight ( <= 1.6kg (3.5lb) )
4.  Inexpensive ( <= $1000 CAD)
5.  Decent keyboard (normal layout/keycap size)
6.  Upgradeable (SSD / Ram)
7.  Battery life (~5 Hours would be nice)
8.  Connectivity (Usb 3.0/Type C, HDMI port, SD card slot)

Your list of priorities probably looks drastically different than mine. For example lots of people value battery life quite highly, and while I understand, I do not mind carrying around the charger.

The reason screen quality and weight are so valuable is to do with my stance on ergonomics. If you are using a computer for many hours in a day, whether for work or for leisure, it is important to take care of your body, particularly the much overlooked hands and eyes. While no laptop keyboard is going to compare to my [Ergodox](www.musicnate.com/ergodorx-layout-and-keybindings.html), small differences over the course of many hours of use can make a significant impact. Same thing goes for screens, where an 11.6", 720p screen may be 'good-enough', if you find yourself squinting as I did, consider how that will influence the health of your eyes. And lastly, I use a messenger bag (I know, I know, poor ergonomics, but there are slim pickings for formal wear backpacks&#x2026;) for transporting my laptop, so a heavier laptop means more uneven stress on my shoulders.

Take a look at the [spreadsheet](#TODO google doc link goes here) I made to compare Chromebooks, and then this [spreadsheet](#TODO link goes here) for a comparison of comparable Windows laptops. You may notice there are some unorthodox devices there which are slightly older. These are mainly just interesting to me for one reason or another, such as the LG Gram which is extraordinarily light (but also delicate!), or the X1 Carbon which would be my perfect device if it wasn't prohibitively expensive.


<a id="org804e391"></a>

# Dual Booting

After putting GalliumOS on my Chromebook, I almost never booted back into ChromeOS. However, there were times when a piece of software is only available on Windows, and would have to use my desktop instead. If you need specific Windows software, or are planning to do any gaming (though I don't know what kind of gaming will be feasible without a dedicated graphics card) then the choice is an obvious one, get a Windows laptop and dual boot linux.

I have seen some posts about dual booting Windows 10 on some Chromebooks, but I haven't personally investigated it.


<a id="org2ec99e2"></a>

# My Top Choices

This is after using an Acer C720 Chromebook with the i3-4005U processor. What drove me to explore different options was the terrible quality screen. Not only was it low resolution, but due to the nature of the TN panel, the viewing angles were incredibly poor, the brightness was low, and the colors were washed out.

My top three choices:

1.  Dell Chromebook 13 / Lenovo Thinkpad (Chromebook) 13
    -   Both of these Chromebooks come in varying models, with processor, ram and screen being upgradeable to suit your needs.
2.  Acer Chromebook 14 (or the 'For Work' edition)
    -   The build quality is said to be quite good, but the performance of the Intel N3160 would not be enough for myself.
    -   While the 'For Work' edition matches the Dell and Lenovo devices in terms of performance, it also matches or exceeds the price.
3.  Lenovo Ideapad 710S (Windows)
    -   A standard laptop ultrabook implementation.

Honorable mentions - Asus Zenbook UX330UA, Dell XPS 13: These two are very popular for a reason, particularly with the developer community.


<a id="org2801db6"></a>

# What did I end up getting?

It would be nice if it there were more options for Linux-only devices, but sadly there are only a select few manufacturers who provide laptops without Windows. You would think it would be cheaper to sell a laptop without Windows, but in one of the few cases where you can buy identical hardware such as the [Dell XPS Developer Edition](#TODO Dell link), it is barely if at all cheaper than its Windows counterpart.

In the end I found a used [Acer Aspire S7-392](http://www.notebookcheck.net/Review-Acer-Aspire-S7-392-Ultrabook.106960.0.html). It hits all of my priorities and at such a discount that I thought it was too good to be true. It has some idiosyncracies such as a dual SSD in RAID 0 on a single mSATA pcb, and a non-standard keyboard layout that for myself is only a minor frustration but could be a deal-breaker for some. The dual SSD in RAID 0 was a stumbling block when installing Linux, as it creates a bunch of weird partitions for Windows and booting. On the other hand it has a super crisp and clear 2560x1440 resolution screen, which also happens to be a touchscreen, and while I can't say that I've made extensive use of the touch feature, it is handy in a pinch.

