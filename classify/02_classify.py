
def _evaluate(y_pred,y_test):
    from sklearn.metrics import classification_report,confusion_matrix
    cr=classification_report(y_test,y_pred)
    print(cr)
    cm=confusion_matrix(y_test,y_pred)
    print(cm)


def evaluate(clf,x_train,y_train,x_test,y_test):
    clf.fit(x_train,y_train)
    y_pred=clf.predict(x_test)
    _evaluate(y_pred,y_test)

if __name__=='__main__':
    import shelve
    import collections
    db = shelve.open('../data/ml_data', 'r')
    x_train, y_train, x_test, y_test = db['02']['data']
    db.close()

    print('========================data_set===========================')
    print('x_train.shape:{}'.format(x_train.shape))
    print('x_test.shape:{}'.format(x_test.shape))
    print('y_train:',collections.Counter(y_train))
    print('y_test:', collections.Counter(y_test))


    print('========================classify===========================')
    from sklearn.svm import SVC
    from sklearn.svm import LinearSVC
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.neighbors import KNeighborsClassifier


    clfs={'linearSVC':LinearSVC(),
          'SVC':SVC(cache_size=3000),
          'RF':RandomForestClassifier(n_estimators=1000),
          'KNN':KNeighborsClassifier(n_neighbors=10)}

    for name,clf in clfs.items():
        print(name)
        evaluate(clf,x_train,y_train,x_test,y_test)

