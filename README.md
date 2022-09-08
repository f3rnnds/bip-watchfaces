# bip-watchfaces

repository with my watchfaces for the Amazfit Bip

# gallery

![](watch_skin_local/gameboy/gameboy_packed_animated.gif)

# install

* install the [Zeep Life](https://play.google.com/store/apps/details?id=com.xiaomi.hm.health) app and sync your device
* copy a watchface directory from [watch_skin_local](watch_skin_local)
* paste to your android storage at `.../Internal shared storage/Android/data/com.xiaomi.hm.health/files/watch_skin_local/`
* Zeep Life > Profile > My devices > Amazfit Bip > Watch face settings > Local watch faces
* select the added watchface
* Sync watch face

# pack

```bash
wget https://bitbucket.org/valeronm/amazfitbiptools/downloads/AmazfitBipTools-1.0.3.1.7z
7z x -o* AmazfitBipTools-1.0.3.1.7z
mono AmazfitBipTools-1.0.3.1/WatchFace.exe gameboy/gameboy.json
python3 fix_header.py gameboy/gameboy_packed.bin
```

# references

* https://www.amazfit.com/en/bip
* https://bitbucket.org/valeronm/amazfitbiptools/
* [Nintendo](www.nintendo.com) Game Boy
