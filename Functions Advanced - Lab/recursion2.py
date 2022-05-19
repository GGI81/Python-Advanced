def loop(index, max_index):
    print(f" -- starting loop ({index, max_index}) -- ")
    if index == max_index:  # base case, exit condition
        print(f" -- ending loop ({index}, {max_index}) -- ")
        return

    print(index)
    loop(index=index + 1, max_index=max_index)
    print(f" -- ending loop ({index}, {max_index}) -- ")


loop(index=0, max_index=10)
