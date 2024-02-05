import os
import random
import shutil

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def makedir(newDir: str) -> None:
    if not os.path.exists(newDir):
        os.makedirs(newDir)


def ListSubDir(path: str) -> [str]:
    entries = os.listdir(path)
    childDir = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
    return childDir


def ListFile(path: str, endWith: str) -> [str]:
    entries = os.listdir(path)
    childDir = [entry for entry in entries if not os.path.isdir(os.path.join(path, entry) and entry.endswith(endWith))]
    return childDir


def GetSubDir(baseDir: str, childDir: str) -> str:
    childDir = os.path.join(baseDir, childDir)
    makedir(childDir)
    return childDir


if __name__ == '__main__':
    oriDir = os.path.join(DATA_DIR, 'origin')
    if not os.path.exists(oriDir):
        print(f'{oriDir} not exist')
        raise Exception(f'{oriDir} not exist')

    testDir = GetSubDir(DATA_DIR, 'test')
    trainDir = GetSubDir(DATA_DIR, 'train')
    validDir = GetSubDir(DATA_DIR, 'valid')

    train_pct = 0.8
    valid_pct = 0.1
    # test_pct = 0.1

    allFile = ListFile(oriDir, '.jpg')
    allLen = len(allFile)
    print(f'Total {allLen} image files')
    assert allLen > 10, 'allLen>10'
    random.shuffle(allFile)
    trainLen = int(allLen * train_pct)
    validLen = int(allLen * (train_pct + valid_pct))

    for i in range(allLen):
        if i < trainLen:
            toFile = os.path.join(trainDir, allFile[i])
        elif i < validLen:
            toFile = os.path.join(validDir, allFile[i])
        else:
            toFile = os.path.join(testDir, allFile[i])
        fromFile = os.path.join(oriDir, allFile[i])
        shutil.copy(fromFile, toFile)

    print(f'Done: {trainLen}, {validLen-trainLen}, {allLen-validLen}')
