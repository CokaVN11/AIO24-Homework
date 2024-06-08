def f1_score(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be an integer.")
        return
    if not isinstance(fp, int):
        print("fp must be an integer.")
        return
    if not isinstance(fn, int):
        print("fn must be an integer.")
        return

    if not (tp > 0 and fp > 0 and fn > 0):
        print("tp, fp, and fn must be greater than zero.")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)

    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1 score is {f1}")


def main():
    f1_score(tp=2, fp=3, fn=4)
    f1_score(tp='a', fp=3, fn=4)
    f1_score(tp=2, fp='a', fn=4)
    f1_score(tp=2, fp=3, fn='a')
    f1_score(tp=0, fp=3, fn=4)
    f1_score(tp=2.1, fp=3, fn=4)


if __name__ == "__main__":
    main()
