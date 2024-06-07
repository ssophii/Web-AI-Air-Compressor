# Web-AI-Air-Compressor
    <h2>Pendahuluan</h2>
    <p><strong>Dataset</strong>: Data Sensor dari Kompresor Udara</p>
    <p><strong>Tujuan</strong>: Memprediksi kegagalan kompresor udara berdasarkan data historis dari sensor.</p>

    <h2>Metodologi</h2>
    <p><strong>Model</strong>: Neural Network dengan arsitektur Sequential dari Keras</p>
    <p><strong>Parameter Tuning</strong>: Tidak disebutkan secara spesifik (model dikompilasi dengan optimizer "rmsprop" dan fungsi loss 'mse')</p>
    <p><strong>Fitur</strong>: Beberapa fitur termasuk aliran udara, tekanan outlet, daya motor, efisiensi, dan lainnya yang diubah menjadi biner dan dinormalisasi.</p>

    <h2>Hasil Evaluasi</h2>
    <p><strong>Mean Squared Error (MSE)</strong>: Tidak disebutkan secara spesifik dalam dokumen</p>

    <h2>Penerapan</h2>
    <p><strong>Framework</strong>: Flask untuk API</p>
    <p><strong>Infrastruktur Monitoring</strong>: Tidak disebutkan secara spesifik (Prometheus dan Grafana tidak disebutkan dalam dokumen)</p>

    <h2>Rekomendasi</h2>
    <p><strong>Monitoring Berkelanjutan</strong>: Lakukan monitoring kinerja model secara berkala.</p>
    <p><strong>Pemeliharaan Model</strong>: Perbarui model secara berkala berdasarkan data terbaru.</p>

    <h2>Detail Tambahan dari Dokumen</h2>
    <p><strong>Proses Data</strong>: Data dari CSV diolah dengan menghapus beberapa kolom dan mengubah beberapa kolom menjadi nilai biner. Data kemudian dinormalisasi sebelum digunakan untuk melatih model.</p>
    <p><strong>Pengembangan Model</strong>: Model jaringan saraf tiruan memiliki beberapa lapisan termasuk input dengan 32 neuron, dua lapisan tersembunyi masing-masing dengan 64 neuron, dan lapisan output dengan 4 neuron.</p>
    <p><strong>Evaluasi Model</strong>: Model dievaluasi menggunakan data yang dinormalisasi dan metrik akurasi juga digunakan.</p>
    <p><strong>Deployment</strong>: Aplikasi Flask memiliki beberapa rute untuk menampilkan halaman utama, ringkasan model, dan prediksi berdasarkan input pengguna. Aplikasi dijalankan dalam mode debug selama pengembangan.</p>
