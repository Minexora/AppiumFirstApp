# Run Appium For Emulator

- Uygulamanın Activity ve package bilgilerini öğrenmek için;
  ```bash
  # Emulatorde uygulama açılıp
  adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'
  # Eğer çalışmaz ise
  dumpsys window | grep -iE "mCurrentFocus=Window{"
  ```

- Uygulamaların indirildiği url  **https://apkcombo.com/** adresidir.
- Inspector **https://github.com/appium/appium-inspector**  adresinden indirilebilir.
- Appium Server **https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4** adresinden indirilebilir.
- Capabilities bilgilerinin detaylarına **https://appium.io/docs/en/writing-running-appium/caps/** adresinden ulaşbilirsiniz.
