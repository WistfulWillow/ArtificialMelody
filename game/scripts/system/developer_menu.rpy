label start:
    if not config.developer:
        jump v1_prolog
    else:
        menu dev_menu_main:
            "Choose a Volume:"
            "Volume 1":
                jump dev_menu_vol1
        menu dev_menu_vol1:
            "Choose a Chapter:"
            "Prologue":
                jump v1_prolog
            "Chapter 1":
                jump dev_menu_vol1_ch1
        menu dev_menu_vol1_ch1:
            "Choose a Day:"
            "Day 1 - Monday 16th September 3095":
                jump ch1_d1_start
            "Day 2 - Tuesday 17th September 3095":
                jump ch1_d2_start
            "Day 3 - Wednesday 18th September 3095":
                jump ch1_d3_start
            "Day 4 - Thursday 19th September 3095":
                jump ch1_d4_start
            "Dreams":
                jump dev_menu_vol1_ch1_dreams
        menu dev_menu_vol1_ch1_dreams:
            "Choose a Dream:"
            "Day 1 - Monday 16th September 3095":
                jump ch1_d1_dream
            "Day 2 - Tuesday 17th September 3095":
                jump ch1_d2_dream