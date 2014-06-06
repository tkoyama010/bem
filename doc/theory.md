成層地盤における静的なグリーン関数
==============================

概要
----

本稿では、多層横方向に等方性または等方性の半空間の静的グリーン関数の計算のための効率的かつ正確な方法を提示します。ベクトル関数とプロパゲータ行列法の円筒システムは、変換ドメインにおいてグリーン関数を導出するために使用されます。プロパゲータ行列で周知の指数関数的に成長要素は、いずれかの上または下にマトリックスを伝搬するソースフィールドの点の相対的な垂直位置に依存することによって分画する。物理ドメインでのグリーン関数を連分数展開した適応的ガウス求積によって数値的に評価されます。数値例は、比較的少ないガウス求積点を得ることができるように非常に正確なグリーン関数を示すために提示される。また、これらの例では、明らかに、変位と応力場に重大な階層化と異方性の効果を示します。

はじめに
-------

変換された領域内のグリーン関数
---------------------------

$$\mathbf{L}\left(r,\theta;\lambda,m\right)=\mathbf{e}_{z}S\left(r,\theta;\lambda,m\right)$$
$$\mathbf{M}\left(r,\theta;\lambda,m\right)=\left(\mathbf{e}_{r}\dfrac{\partial}{\partial\mathbf{r}}+\mathbf{e}_{\theta}\dfrac{\partial}{\mathbf{r}\partial\theta}\right)S\left(r,\theta;\lambda,m\right)$$
$$\mathbf{N}\left(r,\theta;\lambda,m\right)=\left(\mathbf{e}_{r}\dfrac{\partial}{\mathbf{r}\partial\theta}-\mathbf{e}_{\theta}\dfrac{\partial}{\partial\mathbf{r}}\right)S\left(r,\theta;\lambda,m\right)$$
$$S\left(r,\theta;\lambda,m\right)=\dfrac{1}{\sqrt{2\pi}}J_{m}\left(\lambda r\right)e^{im\theta}$$
$$\mathbf{u}\left(r,\theta,z\right)=\sum_{m}\int_{0}^{+\infty}\left[U_{L}\left(z\right)\mathbf{L}\left(r,\theta\right)+U_{M}\left(z\right)\mathbf{M}\left(r,\theta\right)+U_{N}\left(z\right)\mathbf{N}\left(r,\theta\right)\right]\lambda d\lambda$$
$$\mathbf{T}\left(r,\theta,z\right)=\sigma_{rz}\mathbf{e}_{r}+\sigma_{\theta z}\mathbf{e}_{\theta}+\sigma_{zz}\mathbf{e}_{z}$$
$$\mathbf{T}\left(r,\theta,z\right)=\sum_{m}\int_{0}^{+\infty}\left[T_{L}\left(z\right)\mathbf{L}\left(r,\theta\right)+T_{M}\left(z\right)\mathbf{M}\left(r,\theta\right)+T_{N}\left(z\right)\mathbf{N}\left(r,\theta\right)\right]\lambda d\lambda$$
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

