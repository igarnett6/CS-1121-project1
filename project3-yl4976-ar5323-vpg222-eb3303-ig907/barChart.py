from numpy import *
def bar_chart(train, test):
    '''
    Inputs: train, a dictionary of count of each digit of the training set and test, a dictionary of the count
    of each digit for the test set
    Expected Output: A tuple (fig, ax) ready to show using matplotlib
    '''
    num_items_train = 0
    num_items_test = 0
    train_values = []
    test_values = []
    for key in train:
        num_items_train += 1
        num_items_train +=1
    for key in test:
        num_items_test +=1
        test_values.append(test[key])

    y_pos_train = arrange(num_items_train)
    y_pos_test = arrange(num_items_test)

    im1 = plt.bar(y_pos_train, train_values, align = 'center', alpha = .5)
    im2 = plt.bar(y_pos_test, test_values, align = 'center', alpha = .5)

    fig, ax = plt.subplots(2)
    ax[0].imshow(im1, cmap = 'gray')
    ax[0].set_title('Training Set')
    ax[1].imshow(im2, cmap = 'gray')
    ax[1].set_title('Test Set')

    return (fig, ax)
