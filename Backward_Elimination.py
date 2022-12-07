def backward_elimination(dataset):
    best_accuracy = 0
    num_feat = dataset.accur[1]
    """initial empty set"""
    curr_feat = []
    best_feat = []
    for i in range(1,num_feat):
        feat_sub = []
        best_accuracy1 = 0
        for j in range(1, num_feat):
            if best_accuracy1 < accuracy:
                best_accuracy1 = accuracy
                feat_sub = j
            if j not in curr_feat:
                return best_accuracy1
            accuracy = leave_one_out_cross(dataset[:, test_feat])
            test_feat = [n for n in curr_feat if n is not j]
            print("\t\tUsing feature(s) {features} accuracy is {accuracy}%")
            format(features=test_feat, accuracy = accuracy)
        """Removing Classifiers for Backward Elim"""
        if feat_sub:
            curr_feat = [n for n in curr_feat if n is not feat_sub]
            if best_accuracy1 > best_accuracy:
                best_accuracy = best_accuracy1
                best_feat[:] = curr_feat
                print("\nFeature set {} was best, accuracy is {}\n")
                format(curr_feat, best_accuracy1)
            else:
                print("\nFeature set {} was best, accuracy is {}\n")
                format(curr_feat, best_accuracy1)
        print("Finished search!! The best feature subset is {}, which has an accuracy of {}")
        format(best_feat, best_accuracy)