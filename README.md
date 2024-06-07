# Web-AI-Air-Compressor
    Proyek Pemeliharaan Prediktif Kompretor Udara
    
    Pendahuluan
    Dataset: Data Sensor dari Kompresor Udara
    Tujuan: Memprediksi kegagalan kompresor udara berdasarkan data historis dari sensor.
    
    Metodologi
    Model: Neural Network dengan arsitektur Sequential dari Keras
    Parameter Tuning: Model dikompilasi dengan optimizer "rmsprop" dan fungsi loss 'mse'
    Fitur: Beberapa fitur termasuk aliran udara, tekanan outlet, daya motor, efisiensi, dan lainnya yang diubah menjadi biner dan dinormalisasi.
    
    Hasil Evaluasi
    Mean Squared Error (MSE): 0.035858169198036194
    
    Penerapan
    Framework: Flask untuk API
    
    Rekomendasi
    Monitoring Berkelanjutan: Lakukan monitoring kinerja model secara berkala.
    Pemeliharaan Model: Perbarui model secara berkala berdasarkan data terbaru.
    
    Detail Tambahan dari Dokumen
    Proses Data: Data dari CSV diolah dengan menghapus beberapa kolom dan mengubah beberapa kolom menjadi nilai biner. Data kemudian dinormalisasi sebelum digunakan untuk melatih model.
    Pengembangan Model: Model jaringan saraf tiruan memiliki beberapa lapisan termasuk input dengan 32 neuron, dua lapisan tersembunyi masing-masing dengan 64 neuron, dan lapisan output dengan 4 neuron.
    Evaluasi Model: Model dievaluasi menggunakan data yang dinormalisasi dan metrik akurasi juga digunakan.
    Deployment: Aplikasi Flask memiliki beberapa rute untuk menampilkan halaman utama, ringkasan model, dan prediksi berdasarkan input pengguna. Aplikasi dijalankan dalam mode debug selama pengembangan .
