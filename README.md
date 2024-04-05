# Gradient Descent ile Iris Veri Seti Üzerinde Sınıflandırma

Bu proje, gradient inişini (gradient descent) kullanarak iris veri seti üzerinde sınıflandırma işlemi gerçekleştirir. Iris veri seti, çiçeklerin dört özelliğinden (sepal_length, sepal_width, petal_length, petal_width) oluşan bir veri setidir. 

## Gereksinimler

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Veri Seti

Iris veri seti, UCI Machine Learning Repository'de bulunmaktadır. Veri setine [buradan](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) ulaşılabilir. Proje, veri setini otomatik olarak indirmez, bu nedenle veri setini indirip proje klasörüne eklemeniz gerekmektedir.

## Kurulum

1. Projeyi klonlayın:

    ```
    git clone https://github.com/your_username/your_project.git
    ```

2. Proje klasörüne gidin:

    ```
    cd your_project
    ```

3. Gerekli Python paketlerini yükleyin:

    ```
    pip install -r requirements.txt
    ```

## Kullanım

1. Proje klasöründe bulunan `Gradient Descent for Iris.py` dosyasını çalıştırarak gradient inişi ile modeli eğitebilirsiniz.

    ```
    Gradient Descent for Iris.py
    ```

2. Eğitilmiş modelin sonuçlarını görmek için `Gradient Descent for Iris.py` python dosyasını kullanabilirsiniz.

## Model Eğitimi


1. Veri Seti Yüklemesi
Iris veri seti, UCI Machine Learning Repository'den alınır ve önceden tanımlanmış sütun adlarıyla birlikte bir Pandas DataFrame olarak yüklenir.

2. Veri Setini Kontrol Etme
Yüklenen veri seti başlangıçta gözden geçirilir ve ilk beş satır yazdırılarak içeriği kontrol edilir.

3. DataFrame Dönüşümü
Yüklü veri seti, NumPy dizilerine dönüştürülerek işlenmesi kolay hale getirilir.

4. Özellik ve Hedef Değişkeni Ayırma
Veri seti, özellikler (X) ve hedef değişken (y) olarak ayrılır. Özellikler, hedef değişkeni tahmin etmek için kullanılan giriş verileridir.

5. Normalizasyon
Özellikler, her bir özelliğin en küçük ve en büyük değerlerine göre normalleştirilir. Bu, özelliklerin aynı ölçeğe sahip olmasını sağlar ve modelin daha iyi performans göstermesine yardımcı olur.

6. Eğitim ve Test Setlerini Ayırma
Veri seti, eğitim ve test setlerine ayrılır. Eğitim seti, modelin öğrenmek için kullandığı verilerdir, test seti ise modelin performansını değerlendirmek için kullanılır.

7. Gradient Hesaplama Fonksiyonu
Gradient hesaplama fonksiyonu, modelin maliyet fonksiyonuna göre gradyanını hesaplar.

8. Gradyan İnişi Fonksiyonu
Gradyan inişi fonksiyonu, modelin gradyan iniş algoritmasını kullanarak eğitilmesini sağlar. Model, belirlenen öğrenme oranı ve iterasyon sayısı üzerinden eğitilir.
 `gradient_descent.py` dosyasında, gradient inişi algoritması ile model eğitimi gerçekleştirilir.

9. Maliyet Fonksiyonu
Maliyet fonksiyonu, modelin performansını ölçen bir metriktir. Gradyan inişi sırasında maliyet fonksiyonu optimize edilir.

10. Eğitim Maliyetini Görselleştirme
    Modelin eğitim maliyeti, iterasyon sayısına göre çizilerek görselleştirilir. Bu, modelin eğitimi sırasında ne kadar iyi performans gösterdiğini değerlendirmeye yardımcı olur.
 `iris_classification.ipynb` Jupyter Notebook dosyasında, eğitilmiş modelin performansı değerlendirilir ve sonuçlar görselleştirilir.

11. Son Eğitim Maliyeti
Eğitim sürecinin sonunda elde edilen maliyet değeri yazdırılır. Bu değer, modelin ne kadar iyi eğitildiğini gösterir.

