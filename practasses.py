Python 3.10.3 (v3.10.3:a342a49189, Mar 16 2022, 09:34:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

========== RESTART: /Users/admin/Desktop/Tkinter/practiceassesment.py ==========
Traceback (most recent call last):
  File "/Users/admin/Desktop/Tkinter/practiceassesment.py", line 112, in <module>
    main()
  File "/Users/admin/Desktop/Tkinter/practiceassesment.py", line 109, in main
    setup_buttons()
  File "/Users/admin/Desktop/Tkinter/practiceassesment.py", line 91, in setup_buttons
    entry_weather = ttk.Combobox(main_window, textvariable=weather, values=('Sunny', 'Cloudy', 'Rain', 'Snow'), state='readonly')
NameError: name 'ttk' is not defined
