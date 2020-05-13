#Hint: Neural Networks can't just handle the lables as they are, they need --categorical-- data
#Note: You must submit the trained models along with the notebook for full credit
def train_validate_k(x_folds, y_folds, num_folds):
    '''
        Inputs: x_folds, the x folds returned from the k_fold algorithm above,
        y_folds the y folds returned from the k_fold algorithm above
        num_folds, the number of folds used to make the x_folds and y_folds
        Expected Output: Nothing, this function has no explicit output,
        but there must be num_fold models trained and saved to disk
    '''
    for i in range(num_folds-1):
            train_dataset = x_folds[i], y_folds[i]
            validation_dataset = x_folds[i+1], y_folds[i+1]
            train_model(construct_model(), train_dataset, validation_dataset, 20, trained_model)
            break
