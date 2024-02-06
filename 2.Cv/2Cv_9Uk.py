"""
Metoda půlení intervalu hledá řešení obecné rovnice f(x)=0, kdy známe dva body x1 a x2 takové, že f(x1)<0 a f(x2)>0.

    Algoritmus rozpůlí interval mezi body x_1 a x_2,
    tedy nalezne bod x′=x_1+x_22 a pokud je f(x′)<0
    pak nahradí bod x1 bodem x′, jinak nahradí bod x2 bodem x′.

    Výše uvedený krok se opakuje dokud není |x1−x2|<ϵ, kde ϵ je požadovaná přesnost.

    V případě hledání třetí odmocniny z čísla y:

        f(x)=x3−y

    Pokud f(x)=0,

        tak x3−y=0, což lze zapsat jako x3=y a tedy x=3√y

    Napište program, který nalezne třetí odmocninu zadaného čísla y
    na 8 desetinných míst

    (výpočet ukončíte pokud |x1−x2|<0.000000001).

    Na počátku zvolte x1=0 a x2=y pro kladná y>1, x1=y a x2=0 pro záporná y<−1, a x1=−1 a x2=1 v ostatních případech.

"""