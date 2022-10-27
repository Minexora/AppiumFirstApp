# Run Appium Fron Emulator

- Uygulamanın Activity ve package bilgilerini öğrenmek için;
  ```bash
  # Emulatorde uygulama açılıp
  adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'
  # Eğer çalışmaz ise
  dumpsys window | grep -iE "mCurrentFocus=Window{"
  ```
