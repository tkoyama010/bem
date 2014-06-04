成層地盤における静的なグリーン関数
==============================

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

物理領域でのグリーン関数
----------------------

数値計算結果
-----------

####正確な閉形式の解との比較

####異なる数の層を有する半空間の結果の比較

####材料積層効果

####材料異方性の影響

結論
----

