def boxcox_optimise(data, Title=""):
    print(Title)
    print("No transform QQ correlation:",round(probplot(data, rvalue=True)[-1][-1],3) )
    for lambd in range(-5,6):
        if lambd != 0:
            transform = data**lambd
        else:
            transform = np.log(data)
        print(f"lambda={lambd} QQ correlation",round(probplot(transform, rvalue=True)[-1][-1],3))
