def forward_selection(dataset):
    num_feat = dataset.accur[1]
    """initial empty set"""
    curr_feat = []
    best_feat = []
    for i in range(1,num_feat):
        feat_add = []
        """Finding best accuracy"""
        best_accuracy1 = 0
        for j in range(1, num_feat):
            if best_accuracy1 < accuracy:
                best_accuracy1 = accuracy
                feat_add = j
            if j in curr_feat:
                return best_accuracy1
            accuracy = leave_one_out_cross(dataset[:,test_feat])
            test_feat = [0] + curr_feat + [j]
            print("\t\tUsing feature(s) {features} accuracy is {accuracy}%")
            format(features=curr_feat+[j], accuracy = accuracy)
            """Checks for best accuracy"""
        """Adding classifiers for Forward Selection"""
        if feat_add:
            curr_feat.append(feat_add)
            if best_accuracy1 > best_accuracy:
                best_accuracy = best_accuracy1
                best_feat[:] = curr_feat
                print("\nFeature set {} was best, accuracy is {}\n")
                format(curr_feat, best_accuracy)
            else:
                print("\nFeature set {} was best, accuracy is {}\n")
                format(curr_feat, best_accuracy)
        print("Finished search!! The best feature subset is {}, which has an accuracy of {}")
        format(best_feat, best_accuracy)
