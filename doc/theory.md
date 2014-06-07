成層地盤における静的なグリーン関数
==============================

概要
----

本稿では、水平成層または均質な半無限地盤の静的グリーン関数計算法を提案します。
この手法では直行座標系におけるグリーン関数を導出するために円筒座標系における伝達マトリックスを使用します。
この伝達マトリックスにおける指数関数項は、上下いずれかに行列を増やすことにより離散化します。
それらの行列は加振点との相対的な垂直位置に依存します。
次に、物理領域でのグリーン関数を級数展開したガウス求積法によって数値的に評価します。
最後に数値計算例により、比較的少ないガウス積分点により精度の高いグリーン関数が計算できることを示します。
また、これらの例では、変位と応力場における階層化と異方性の効果を示します。

はじめに
-------

変換された領域内のグリーン関数
---------------------------

半無限地盤の上にある$p-1$層の水平成層地盤を考えます。
最上部の層を$1$、その下の層も順番に番号を付けていき、下部領域を層$P$とします。
座標系は地表面を原点、z軸が鉛直方向下向きの円筒座標系とします。
$k$番目の層には$z=0,z_{p-1}$における境界条件があります。
各層の座標系は$z=0$から$z=H$です、ただし$H$は層の厚さです。
ベクトル関数の円筒座標系における式は次のようになります。

$$\mathbf{L}\left(r,\theta;\lambda,m\right)=\mathbf{e}_{z}S\left(r,\theta;\lambda,m\right)$$

$$\mathbf{M}\left(r,\theta;\lambda,m\right)=\left(\mathbf{e}_{r}\dfrac{\partial}{\partial\mathbf{r}}+\mathbf{e}_{\theta}\dfrac{\partial}{\mathbf{r}\partial\theta}\right)S\left(r,\theta;\lambda,m\right)$$

$$\mathbf{N}\left(r,\theta;\lambda,m\right)=\left(\mathbf{e}_{r}\dfrac{\partial}{\mathbf{r}\partial\theta}-\mathbf{e}_{\theta}\dfrac{\partial}{\partial\mathbf{r}}\right)S\left(r,\theta;\lambda,m\right)$$

ただし、

$$S\left(r,\theta;\lambda,m\right)=\dfrac{1}{\sqrt{2\pi}}J_{m}\left(\lambda r\right)e^{im\theta}$$

ここで、$J_m(\lambda r)$は$m$次のBessel関数です。
$m=0$は軸対称変形に対応します。

上記の円筒座標系は、完全な直交空間を形成するので、任意のベクトル積分関数で表すことができます。
具体的には、変位ベクトルと引張応力は次式となります。

$$\mathbf{u}\left(r,\theta,z\right)=\sum_{m}\int_{0}^{+\infty}\left[U_{L}\left(z\right)\mathbf{L}\left(r,\theta\right)+U_{M}\left(z\right)\mathbf{M}\left(r,\theta\right)+U_{N}\left(z\right)\mathbf{N}\left(r,\theta\right)\right]\lambda d\lambda$$

$$\mathbf{T}\left(r,\theta,z\right)=\sigma_{rz}\mathbf{e}_{r}+\sigma_{\theta z}\mathbf{e}_{\theta}+\sigma_{zz}\mathbf{e}_{z}=\sum_{m}\int_{0}^{+\infty}\left[T_{L}\left(z\right)\mathbf{L}\left(r,\theta\right)+T_{M}\left(z\right)\mathbf{M}\left(r,\theta\right)+T_{N}\left(z\right)\mathbf{N}\left(r,\theta\right)\right]\lambda d\lambda$$

さらに、釣り合い方程式と構成則に式を代入することで、連立微分方程式の2つの独立した式が得られます。

$$\left[E^{I}\left(z\right)\right]=\left[Z^{I}\left(z\right)\right]\left[K^{I}\right]$$

$$\left[E^{II}\left(z\right)\right]=\left[Z^{II}\left(z\right)\right]\left[K^{II}\right]$$

$$\left[E^{I}\left(z\right)\right]=\left\{\begin{array}{c}U_{L}\left(z\right)\\\lambda U_{M}\left(z\right)\\\dfrac{T_{L}\left(z\right)}{\lambda}\\T_{M}\left(z\right)\end{array}\right\}$$

$$\left[E^{II}\left(z\right)\right]=\left\{\begin{array}{c}U_{N}\left(z\right)\\\dfrac{T_{N}\left(z\right)}{\lambda}\end{array}\right\}$$

$$\left[K^{I}\right]=\left\{\begin{array}{c}c_{1}\\c_{2}\\c_{3}\\c_{4}\end{array}\right\}$$

$$\left[K^{II}\right]=\left\{\begin{array}{c}c_{5}\\c_{6}\end{array}\right\}$$

$$\left[E^{I}\left(z_{k-1}\right)\right]=\left[a^{I}\right]\left[E^{I}\left(z_{k}\right)\right]$$

$$\left[E^{II}\left(z_{k-1}\right)\right]=\left[a^{II}\right]\left[E^{II}\left(z_{k}\right)\right]$$

$$f_{j}\left(r,\theta,z\right)=\dfrac{\delta\left(r\right)\delta\left(\theta\right)\delta\left(z-h\right)}{r}n_{j};j=r,\theta,z$$

$$\Delta T_{L}=T_{L}\left(h+0\right)-T_{L}\left(h-0\right)=\dfrac{-n_{z}}{\sqrt{2\pi}};m=0$$

$$\Delta T_{M}=T_{M}\left(h+0\right)-T_{M}\left(h-0\right)=\dfrac{\pm n_{x}+in_{y}}{2\lambda\sqrt{2\pi}};m=\pm1$$

$$\Delta T_{N}=T_{N}\left(h+0\right)-T_{N}\left(h-0\right)=\dfrac{in_{x}\pm n_{y}}{2\lambda\sqrt{2\pi}};m=\pm1$$

$$\left[E^{I}\left(z\right)\right]=\left[a_{k}^{I}\left(z-z_{k-1}\right)\right]\left[a_{k+1}^{I}\right]\cdots\left[a_{p-1}^{I}\right]\left[Z_{p}^{I}\left(H\right)\right]\left[K^{I}\right]$$

$$\left[E^{II}\left(z\right)\right]=\left[a_{k}^{II}\left(z-z_{k-1}\right)\right]\left[a_{k+1}^{II}\right]\cdots\left[a_{p-1}^{II}\right]\left[Z_{p}^{II}\left(H\right)\right]\left[K^{II}\right]$$

$$\left[a_{k}^{I}\left(z_{k}-z_{k-1}\right)\right]=\left[b_{k}^{I}\left(z_{k}-z_{k-1}\right)\right]exp\left\{ \lambda\left(z_{k}-z_{k-1}\right)\right\}$$

$$\left[a_{k}^{II}\left(z_{k}-z_{k-1}\right)\right]=\left[b_{k}^{II}\left(z_{k}-z_{k-1}\right)\right]exp\left\{ \lambda\left(z_{k}-z_{k-1}\right)\right\}$$

物理領域でのグリーン関数
------------------------

$$\int_{0}^{+\infty}f\left(\lambda,z\right)J_{m}\left(\lambda r\right)d\lambda=\sum_{n=1}^{N}\int_{\lambda_{n}}^{\lambda_{n+1}}f\left(\lambda,z\right)J_{m}\left(\lambda r\right)d\lambda$$

数値計算結果
-----------

####正確な閉形式の解との比較

####異なる数の層を有する半空間の結果の比較

####材料積層効果

####材料異方性の影響

結論
----

