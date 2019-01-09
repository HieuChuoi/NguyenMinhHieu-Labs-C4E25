from matplotlib import pyplot

ref_name = ["Events", "Ads", "WOM"]
ref_count = [3902, 1938, 1132]

pyplot.pie(ref_count, labels=ref_name, autopct="%.1f%%", shadow=True)
pyplot.axis("equal")
pyplot.show()