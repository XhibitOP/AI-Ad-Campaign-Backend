def calculate_roas(ctr, cpc):
    if cpc == 0:
        return 0
    return round((ctr * 100) / cpc, 2)