def plot_two(im1, title1, im2, title2):
    '''
        Input: im1, a matrix representing a grayscale image and title1 a string,im2 a matrix representing
        a grayscale image and title2 a string
        Expected Output: A tuple (fig, ax) representing a generated figure from matplotlib and two subplots
        ready to display the inputed images with the given titles
    '''
    fig, ax = plt.subplots(2)
    ax[0, 1].imshow(im1, cmap=gray)
    ax[0,1].set_title(title1)
    ax[0,2].imshow(im2)
    ax[0,2].set_title(title2)

    return (fig, ax)

plot_two(lc_train, 'Least Common Train', lc_test, 'Least Common Test'), plot_two(mc_train, 'Most Common Train', mc_test, 'Most Common Test')
plt.show()
