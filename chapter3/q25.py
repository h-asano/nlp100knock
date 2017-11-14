"""
{{基礎情報 国
|略名 = イギリス
|日本語国名 = グレートブリテン及び北アイルランド連合王国
|公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>
*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>
"""
import sys
import json


def main():
    dic = extract_baseinf(sys.stdin)
    sys.stdout.write(json.dumps(dic, ensure_ascii=False))
    for k, v in dic.items():
        print(k, v, file=sys.stderr)


def extract_baseinf(fi):
    baseinf = {}
    isbaseinf = False
    for line in fi:
        if isbaseinf:
            if line.startswith('}}'):
                return baseinf

            elif line[0] == '|':
                templis = line.strip('|\n').split('=')
                key = templis[0].strip()
                value = "=".join(templis[1:])
                baseinf[key] = value
                
            else:
                baseinf[key] += '\n{}'.format(line.rstrip('\n'))

        elif line.startswith('{{基礎情報'):
            isbaseinf = True


if __name__ == '__main__':
    main()