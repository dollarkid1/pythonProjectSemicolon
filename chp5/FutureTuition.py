year = 0
tuition = 10_000
while tuition <= 20000:
    year += 1
    tuition = tuition * 1.07
    
print(f"\nTuition will be doubled in {str(year)} years and will at ${format(tuition, '.2f')}")