duration = int(input("Введите продолжительность времени, в секундах: "))

days = duration // (60 * 60 * 24)
hours = (duration - days * (60 * 60 * 24))// (60 * 60)
minutes = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
seconds = duration - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60
print(f"Продолжительность времени равна: {days}дней, {hours}часов, {minutes}минут, {seconds}секунд")




