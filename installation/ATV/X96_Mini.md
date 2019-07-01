# <strong>X96 Mini</strong> (<strong>S905W 2GB/16GB)</strong>

<strong>Image: </strong>s905<strong>w</strong>_atvXperience_v2<strong>FF</strong>

<h2><a href="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/x96_mini-preview.jpg"><img class="aligncenter size-thumbnail wp-image-258" src="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/x96_mini-preview-150x150.jpg" alt="" width="150" height="150" /></a></h2>

<hr />
<p style="text-align: center;"><strong>CAUTION</strong><p>Make sure to download firmware for S905<strong>W</strong> <strong>(NOT X!)</strong></p>
<p style="text-align: center;">X96 Mini <strong>S905W 2GB/16GB</strong></p>
<p style="text-align: center;"><a href="https://www.amazon.de/Smart-Box-Android-7-1-USB-Anschluss-Schwarz/dp/B078ZF9YT6/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&amp;keywords=x96+mini+2gb&amp;qid=1559678255&amp;s=gateway&amp;sr=8-4">Amazonlink</a></p>
<h6 style="text-align: center;"><em>If you try this on a wrong model - you could brick your ATV Box!<p>
<strong>!READ CAREFULLY!</strong></em></h6>

<hr />

<h3>Prerequisite:</h3>
<ul>
 	<li>X96 Mini (<strong>S905W)</strong></li>
 	<li>Windows 7-10 Environment</li>
 	<li>2GB+ SD Card</li>
 	<li>Cardreader</li>
 	<li>brain.ps1</li>
 	<li>Toothpick</li>
 	<li>USB Keyboard + Mouse</li>
 	<li>Needed Downloads:</li>
<ul>
 	<li>s905<strong>w</strong>_atvXperience_v2<strong>FF </strong>Image.img [ <a href="https://mega.nz/#F!GEpQmQhZ!ezNEXQdnyNIhm2axjnfTIg?2IYzQShJ">here</a> ]</li>
 	<li>Burn_Card_Maker.exe [ <a href="https://share108.com/06r0pntu2p6h/Burn_Card_Maker%E5%B7%A5%E5%85%B7.rar">here</a> ] [ <a href="https://www.mediafire.com/?v28g81wjx25dyk3">here</a> ] or [ <a href="http://www.filefactory.com/file/7d4u08th9qpn/Burn_Card_Maker%E5%B7%A5%E5%85%B7.rar">here</a> ]</li>
 	<li>Magisk-v18.1.zip [ <a href="https://github.com/topjohnwu/Magisk/releases">here</a> ]</li>
 	<li>MagiskManager-v7.0.0.apk [ <a href="https://github.com/topjohnwu/Magisk/releases">here</a> ]</li>
 	<li>SmaliPatcherModule-0.0.4.9-fOmeyXDA - <strong>IMPORTANT</strong>: Use this file ONLY for this project! [ <a href="https://bl.pixlmap.de/download_smali/SmaliPatcherModule_for_X96mini-s905w_ATV_XDA.zip">here</a> ]</li>
</ul><p>
 	<li><em>Optional Downloads:</em>
<ul>
 	<li><em>PogoDroid.apk [ <a href="https://www.maddev.de/apk/PogoDroid.apk">here</a> ]</em></li>
 	<li><em>RemoteGpsController.apk [ <a href="https://github.com/Map-A-Droid/MAD/blob/master/APK/RemoteGpsController.apk">here</a> ]</em></li>
 	<li><em>Teamviewer.apk [ <a href="https://download.teamviewer.com/download/TeamViewer.apk">here</a> ]</em></li>
 	<li><em>"Yourgame" 145.1 APK [ <a href="https://www.apkmirror.com/apk/niantic-inc/pokemon-go/pokemon-go-0-145-1-release/pokemon-go-0-145-1-android-apk-download/download/">here</a> ]</em></li>
 	<li><em>link2sd-4-0-13.apk [ <a href="https://www.apkmirror.com/?post_type=app_release&amp;searchtype=apk&amp;s=link2sd">here</a> ]</em></li>
</ul>
</li>
</ul>
</li>
</ul>

<hr />

<h3>Prepare your SD Card:</h3>
<h4><strong>** Important **</strong></h4>
Make sure youre formatting your SD Card with a <strong>FAT16</strong> partitionschema - <strong>otherwise the flash will fail on 10% with a red X under the Android.</strong>
<p>
<ul>
 	<li>Start <em>compmgmt.msc</em></li>
 	<li>Navigate -&gt; Disk Management (Datenträgerverwaltung)</li>
 	<li>Look for SD Card</li>
 	<li>Delete the whole (f.e. 8GB) partition</li>
 	<li>Create a new one with 4000MB</li>
 	<li>format with FAT16</li>
</ul>
<a href="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/fat16.png"><img class="wp-image-229 size-full" src="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/fat16.png" alt="" width="490" height="383" /></a>

<hr />

<h3>Flash ATVX to SD:</h3>
<ul>
 	<li>Start Burn_Card_Maker.exe
<ul>
 	<li>Hit the menu and tick english language</li>
 	<li>

<a href="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/burnen.png"><img class="wp-image-226 " src="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/burnen.png" alt="" width="225" height="211" /></a></li>
</ul>
</li>
</ul>
&nbsp;
<ul>
 	<li>Flash the s905w_atvXperience_v2FF Imagefile with Burn_Card_Maker with '<em>make</em>'</li>
</ul>
<a href="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/burncardmaker2.png"><img class="wp-image-181 aligncenter" src="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/burncardmaker2.png" alt="" width="405" height="291" /></a>

<hr />

<h3>Copy Apks and Zip's to your SD Card after a succeeded flash:</h3>
<ul>
 	<li>Magisk-v18.1.zip</li>
 	<li>MagiskManager-v7.0.0.apk</li>
 	<li>SmaliPatcherModule-0.0.4.9-fOmeyXDA.zip</li>
 	<li><em>link2sd-4-0-13.apk</em></li>
 	<li><em>PogoDroid.apk</em></li>
 	<li><em>RemoteGpsController.apk</em></li>
</ul>

<hr />

<h3>Booting into flashingmode:</h3>
<ul>
 	<li>Shutdown X96</li>
 	<li>Put your <strong>SD</strong> Card <strong>into</strong> the X96</li>
 	<li>Use a <strong>toothpick</strong> and <strong>hold</strong> the button <em>inside</em> the <strong>AV </strong>slot!</li>
 	<li><strong>Add</strong> <strong>DC</strong></li>
 	<li>X96 should boot directly into <strong>Flashingmode</strong></li>
 	<li><strong>release</strong> <strong>toothpick</strong></li>
 	<li>let the <strong>flash</strong> process end</li>
 	<li>X96 Mini should reboot</li>
</ul>
<strong>After a while (grab a <em>new</em> coffee) you'll see a 'welcome message' - if so: you're good!</strong>

<hr />

<h3>Flash Magisk and Smalipatcher:</h3>
<ul>
 	<li>Boot into TWRP -recoverymode:
<ul>
 	<li>Shutdown X96</li>
 	<li>Remove SD Card (Important!)</li>
 	<li>Toothpick -&gt; AVbutton + DC</li>
 	<li>After a while <strong>TWRP</strong> will show its gui</li>
 	<li>Put in SD Card</li>
</ul>
</li>
 	<li>Use <em>install</em>
<ul>
 	<li>Flash Magisk-v18.1.zip <strong>and</strong> SmaliPatcherModule-0.0.4.9-fOmeyXDA.zip</li>
 	<li>Clear Dalvik/Cache <strong>and</strong> reboot</li>
</ul>
</li>
 	<li>Remove SD Card</li>
 	<li>Install the MagiskManager.apk via the AppDrawer/Dateien and start Magisk</li>
 	<li><strong>Important</strong>: Deactivate buildinroot (AppDrawer/Einstellungen/SuperUser/off)
<ul>
 	<li>Check SafetyNet</li>
</ul>
</li>
 	<li>Have fun!</li>
</ul>
<a href="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/magisk-1.png"><img class="wp-image-193 " src="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/magisk-1.png" alt="" width="366" height="236" /></a> 

<hr />

<blockquote>
<h3><strong>If youre here, you know what to do to run your favorite game on a ATV ;)</strong></h3>
</blockquote>

<hr />

<h3>Hint:</h3>
<ul>
 	<li>Recommend RJ45 connection</li>
 	<li><strong>If you want to scan quests</strong> - Use Portaitmode<li>
 	<li>Switch to 480p res if you're ready to go (Settings/Display/Screen Resolution/Display Mode)</li>
 	<li>Use Teamviewer.apk to remote control your games (Some games don't reacting on keyboards) or use <strong>scrcpy</strong>!</li>
 	<li>Uninstall all useless Apps on the X96 (pretty simple via Teamviewer)</li>
</ul>
<a href="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/app_atv.png"><img class="wp-image-179 " src="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/app_atv.png" alt="" width="644" height="494" /></a> 

<a href="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/installeapp.png"><img class="wp-image-188 " src="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/installeapp.png" alt="" width="664" height="250" /></a> 

<a href="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/runningmad.png"><img class="wp-image-190 " src="https://pixlblog.pixlmap.de/wp-content/uploads/2019/06/runningmad.png" alt="" width="224" height="104" /></a>

# Contribute
If you know it better, feel free to PR your wisdom
