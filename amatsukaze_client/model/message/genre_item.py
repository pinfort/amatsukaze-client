from dataclasses import dataclass


@dataclass
class GenreItem():
    """
    Level1==0xE(拡張)かどうかで入れられる値が変わる
    拡張でない場合
        Space は GenreSpace.ARIB
        Level1,Level2は通常のLevel1,Level2
    拡張の場合
        Space は Level2 + 1
        Level1,Level2はUser1,User2
    SpaceはGenreSpaceが対応しているが、事業者定義の値であるため
    GenreSpaceにない値が使用されることがあるのでint型とする
    （GenreSpaceにするとシリアライズでエラーとなるので）
    """
    space: int
    level1: int
    level2: int
