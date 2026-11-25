# Modul 08: Solution Architecture & Integration

## 1. Identitas Modul

| Atribut | Keterangan |
|---------|------------|
| **Kelompok Jalur** | Jalur Alternatif — Business & System Analysis (Jilid II: *Business Analysis, System Design & Product Strategy*) |
| **Level Kompetensi** | Senior (setara standar *Senior Solution Architect*, *TOGAF® / AWS–GCP Solutions Architect Professional*, dan *Enterprise Integration Specialist*) |
| **Durasi Pembelajaran** | **12 jam sesi terstruktur** (4 sesi × 3 jam) + **±6 jam tugas mandiri** |
| **Prasyarat** | Telah menyelesaikan **Modul 06** (*Business Analysis & Requirements Engineering*) dan **Modul 07** (*System Analysis, Modeling & Data Design*) |
| **Peran Sasaran** | Senior Solution Architect (SA), Lead System Analyst, Technical Project Manager, Engineering Manager, Enterprise Architect, serta Senior PM/BA yang berkolaborasi langsung dalam keputusan arsitektur, integrasi *legacy*, dan kendali biaya *cloud* |
| **Keluaran Utama** | 1) *Solution Architecture Blueprint & API Contract Matrix* (REST + Event Schema), 2) *Polyglot Persistence & Capacity Sizing Plan* (2.500 TPM), 3) *Architecture Decision Record* (ADR), dan 4) *Cloud Multi-AZ, Disaster Recovery (RPO/RTO) & UU PDP/PCI-DSS Security Readiness Plan* pada konteks **Proyek OMNI** |

---

## 2. Gambaran Modul

Pada Modul 06 dan Modul 07, Anda telah menerjemahkan strategi omnichannel **PT Sinar Nusantara Retail Tbk (SNR)** menjadi spesifikasi kebutuhan bisnis (*BRD/FRD*), *User Stories*, model perilaku sistem (*UML Sequence & Activity Diagram*), serta skema data konseptual (*ERD*). Namun, di dunia nyata transformasi digital berskala korporasi, spesifikasi kebutuhan yang sempurna dan model data yang rapi belum menjamin sistem mampu bertahan saat diserbu puluhan ribu pelanggan pada malam puncak Harbolnas 12.12. Di sinilah disiplin **Solution Architecture & Integration** mengambil peran sebagai jembatan penentu antara *apa yang dibutuhkan bisnis* dan *bagaimana sistem dibangun, diintegrasikan, diamankan, serta dioperasikan secara andal dan ekonomis*.

Bayangkan kompleksitas teknis yang dihadapi **Dimas Prasetyo** (Lead Solution Architect Proyek OMNI) bersama **Irwan Pratama** (CTO PT SNR). Proyek OMNI bukan aplikasi *startup* yang dibangun dari nol di ruang hampa (*greenfield*). Sistem baru—aplikasi mobile iOS/Android, web e-commerce, *Order Management System* (OMS), *Click & Collect* (BOPIS), dan *Digital Loyalty Engine*—harus beroperasi **≥ 99,5% uptime**, lulus uji beban **2.500 transaksi/menit (TPM)**, dan menjaga sinkronisasi stok **≤ 60 detik** sambil terhubung dengan sistem *legacy* yang sedang berjalan: **120 toko fisik di 24 kota** (yang sebagian koneksi internetnya di luar Jawa tidak stabil), **3 Distribution Center** (Cikarang, Surabaya, Medan) di bawah **Siti Rahmawati**, dua proyek paralel (**ERP-Refresh** dan **POS-Modern**), *Payment Gateway* **PT FinPay Nusantara** (standar PCI-DSS), proyek hilir **DataHub**, serta pengawasan ketat kepatuhan **UU PDP No. 27/2022** dari **Rina Kartika**—semuanya di dalam pagu anggaran Integrasi **CB-02 Rp 1,65 M** dan Infrastruktur/Keamanan/Perangkat Toko **CB-03 Rp 1,15 M**.

Modul 08 membekali Anda dengan pola pikir arsitek solusi senior berbasis ***trade-off analysis***: tidak ada arsitektur yang "sempurna untuk semua situasi", yang ada hanyalah arsitektur yang paling selaras dengan *Non-Functional Requirements* (NFR), kendala anggaran, kapabilitas tim (18 personel vendor **PT Nusantara Digital Solusi / PT NDS** di bawah **Bambang Hartono** ditambah tim IT internal SNR), serta tenggat mutlak **26 November 2027**. Anda akan mendalami desain API modern, strategi *polyglot database* dan *caching*, keputusan krusial antara *Modular Monolith* versus *Microservices*, pola integrasi *event-driven* dan ketahanan (*Circuit Breaker, Saga, Outbox, ACL*), topologi *Cloud High Availability Multi-AZ* Region Jakarta dan *Disaster Recovery* (RPO/RTO), keamanan *Defense-in-Depth* dan *Observability*, hingga cara mendokumentasikan keputusan arsitektur yang objektif melalui **Architecture Decision Record (ADR)** di hadapan CTO dan *Steering Committee*.

---

## 3. Capaian Pembelajaran

Setelah menyelesaikan Modul 08, peserta mampu:

1. **Merancang** antarmuka pemrograman aplikasi (*API*) modern berpendekatan *Contract-First* (RESTful, *idempotency*, *versioning*, OpenAPI), memilih secara tepat antara REST, GraphQL, gRPC, dan Webhook, serta menetapkan peran *API Gateway* dan *Backend for Frontend* (BFF).
2. **Menentukan** strategi *Polyglot Persistence*, *caching*, replikasi baca, dan *partitioning* berdasarkan karakter transaksi dan **CAP Theorem** guna mencapai target sinkronisasi stok ≤ 60 detik dan bebas *overselling* pada beban 2.500 TPM.
3. **Mengevaluasi** gaya arsitektur (*Monolith, Modular Monolith, Microservices*) berdasarkan *Domain-Driven Design* (*Bounded Contexts*), *Conway's Law*, dan ukuran tim, serta menerapkan pola **Strangler Fig** untuk memodernisasi sistem *legacy* tanpa menghentikan operasi 120 toko.
4. **Merancang** arsitektur integrasi perusahaan (*Enterprise Integration Patterns*) yang memadukan komunikasi sinkron dan asinkron (*Event-Driven Architecture*), dilengkapi pola ketahanan (**Circuit Breaker, Retry with Backoff & Jitter, DLQ, Transactional Outbox, Saga**, dan **Anti-Corruption Layer**).
5. **Menyusun** rancangan infrastruktur *Cloud* berbasis *High Availability Multi-AZ* (Region Jakarta), target *Disaster Recovery* (**RPO/RTO**), *auto-scaling*, dan disiplin **FinOps** yang selaras dengan pagu anggaran serta kepatuhan **UU PDP**, **PCI-DSS**, **OWASP API Security**, dan 3 pilar **Observability**.
6. **Menulis** **Architecture Decision Record (ADR)** yang terstruktur, kuantitatif, dan transparan untuk mempertahankan *trade-off* arsitektur di hadapan CTO, *Steering Committee*, dan mitra vendor implementasi.

---

## 4. Rencana Sesi

Pembelajaran tatap muka atau lokakarya daring dilaksanakan dalam **4 sesi × 3 jam = 12 jam** dengan komposisi pedagogis **±30% konsep (3,5 jam)**, **±50% workshop kasus Proyek OMNI (6,0 jam)**, dan **±20% diskusi/refleksi arsitektural (2,5 jam)**.

| Sesi | Durasi | Topik Utama | Konsep (±30%) | Workshop Kasus (±50%) | Diskusi & Refleksi (±20%) |
|------|--------|-------------|---------------|-----------------------|---------------------------|
| **Sesi 1** | 3 jam | **Arsitektur API Modern, API Gateway, BFF & Polyglot Persistence** | 55 menit: Prinsip RESTful, *Idempotency*, REST vs GraphQL vs gRPC vs Webhook; API Gateway & BFF; SQL vs NoSQL, Redis, Elasticsearch, *Caching* & CAP Theorem | 90 menit: Merancang 5 kontrak API inti Proyek OMNI (OpenAPI/JSON) & merakit strategi *Polyglot Persistence* + perhitungan *throughput* 2.500 TPM / 125 TPS *burst* | 35 menit: Bedah kasus kegagalan *double-order* tanpa *Idempotency-Key* & bahaya *Cache Stampede* saat *flash sale* |
| **Sesi 2** | 3 jam | **Gaya Arsitektur Aplikasi, DDD Bounded Contexts & Strangler Fig** | 50 menit: *Monolith* vs *Modular Monolith* vs *Microservices*; jebakan *Distributed Monolith*; DDD *Bounded Contexts*; *Strangler Fig Pattern* untuk *legacy* | 90 menit: Memetakan *Bounded Contexts* Proyek OMNI & menyusun **ADR-001** menilai usulan vendor PT NDS (18–25 *microservices* vs 6 *modular services*) | 40 menit: Debat simulasi *Architecture Review Board* antara Lead SA (Dimas), Vendor (Bambang), dan CTO (Irwan) |
| **Sesi 3** | 3 jam | **Enterprise Integration Patterns, Event-Driven & Resilience** | 55 menit: Sinkron vs Asinkron (Kafka/PubSub); *Circuit Breaker*, *Retry + Jitter*, DLQ, *Transactional Outbox*, *Saga* (Choreography vs Orchestration), dan ACL | 90 menit: Merancang skema *event* `inventory.updated`, alur *Saga* pembatalan *Click & Collect*, serta parameter *Circuit Breaker* untuk 15 toko luar Jawa | 35 menit: Analisis *post-mortem* *Cascading Failure* akibat rantai panggilan sinkron (*Chatty Synchronous Chains*) ke ERP lama |
| **Sesi 4** | 3 jam | **Cloud Multi-AZ, DR (RPO/RTO), FinOps, Keamanan UU PDP & Observability** | 50 menit: IaaS/PaaS/SaaS & Kubernetes; HA Multi-AZ vs DR (4 tingkat RPO/RTO); FinOps; *Defense-in-Depth* (TLS 1.3, KMS, PCI-DSS, UU PDP, OWASP API); 3 Pilar *Observability* | 90 menit: Menyusun topologi Cloud Region Jakarta, menghitung anggaran *downtime* 99,5% vs biaya DR terhadap pagu CB-03 Rp 1,15 M, & daftar periksa audit Rina Kartika | 40 menit: Evaluasi 5 *Architecture Anti-Patterns*, kuis cepat pemantapan, dan *briefing* tugas mandiri ±6 jam |
| **Total** | **12 jam** | **4 Sesi Terpadu** | **3,5 jam (29%)** | **6,0 jam (50%)** | **2,5 jam (21%)** |

---

## 5. Materi

![Arsitektur Solusi Cloud, API Gateway, Microservices, dan Integrasi Event-Driven Proyek OMNI](assets/images/fig-08-cloud-microservices-api.jpg)

*Gambar 5.0 — Ilustrasi Panorama Arsitektur Solusi Cloud-Native, API Gateway/BFF, Domain Services, Polyglot Data, dan Integrasi Event-Driven pada Proyek OMNI PT Sinar Nusantara Retail.*

Seorang *Senior Solution Architect* tidak mengukur keberhasilan rancangannya dari seberapa mutakhir teknologi yang ditempelkan di slide presentasi, melainkan dari seberapa presisi arsitektur tersebut memenuhi **atribut kualitas (*Quality Attributes* / NFR)** bisnis—kinerja, ketersediaan, skalabilitas, keamanan, keterpeliharaan, dan efisiensi biaya—secara seimbang. Mark Richards dan Neal Ford merumuskan **Hukum Pertama Arsitektur Perangkat Lunak** (*First Law of Software Architecture*): *"Segala sesuatu dalam arsitektur perangkat lunak adalah trade-off; jika seorang arsitek merasa menemukan solusi tanpa trade-off, berarti ia belum menemukan trade-off-nya."*

Sebelum membedah setiap lapisan arsitektur secara mendalam, mari kita pahami terlebih dahulu **Topologi Arsitektur Solusi End-to-End Proyek OMNI** yang menjadi peta besar seluruh pembahasan modul ini.

```mermaid
flowchart TD
    subgraph CLIENTS["Lapisan Klien (Channels)"]
        MOB["Aplikasi Mobile<br/>iOS & Android (500 rb MAU)"]
        WEB["Web E-Commerce<br/>Responsif & SEO"]
        TAB["Store Fulfillment App<br/>240 Tablet di 120 Toko"]
    end

    subgraph EDGE["Lapisan Edge & Keamanan"]
        CDN["CDN & Edge Cache<br/>Aset Statis & Gambar SKU"]
        WAF["Cloud WAF & DDoS Shield<br/>TLS 1.3 Termination"]
    end

    subgraph GW["API Gateway & Backend for Frontend (BFF)"]
        APIGW["API Gateway (Kong / Cloud GW)<br/>OAuth 2.0 / OIDC / JWT & Rate Limit"]
        BFFM["Mobile BFF<br/>Payload Ringkas"]
        BFFW["Web BFF<br/>SSR & SEO Data"]
        BFFS["Store Ops BFF<br/>Offline-Resilient Sync"]
    end

    subgraph CORE["Layanan Domain Inti Proyek OMNI (Managed Kubernetes - Jakarta)"]
        CAT["Catalog & Search Service<br/>18.500 SKU"]
        INV["Inventory & Reservation Service<br/>Sync ≤ 60 Detik"]
        OMS["OMS & BOPIS Orchestrator<br/>Saga Order & Click-Collect"]
        LOY["Digital Loyalty Service<br/>Poin, Tier & QR Voucher"]
        PAY["Payment & Shipping Adapter<br/>Tokenisasi & Kurir"]
        NOTIF["Notification Service<br/>Push, Email, WhatsApp"]
    end
    subgraph BUS["Event Bus & Integrasi Asinkron"]
        KAFKA["Message Broker / Event Bus<br/>Apache Kafka / Cloud PubSub + DLQ"]
    end
    subgraph ACL_LAYER["Anti-Corruption Layer (ACL) & Mitra Eksternal"]
        ACLERP["ACL ERP & WMS<br/>ERP-Refresh & 3 DC"]
        ACLPOS["ACL POS Adaptor<br/>POS-Modern 120 Toko"]
        FINPAY["PT FinPay Nusantara<br/>Payment Gateway PCI-DSS"]
        COURIER["Agregator Kurir<br/>Reguler & Instan"]
        DATAHUB["Proyek DataHub (PRJ-04)<br/>Data Warehouse & Analitik"]
    end
    MOB --> CDN --> WAF --> APIGW
    WEB --> CDN
    TAB --> WAF
    APIGW --> BFFM --> CAT
    APIGW --> BFFW --> OMS
    APIGW --> BFFS --> INV
    BFFM --> OMS
    BFFM --> LOY
    BFFW --> CAT
    BFFS --> OMS
    OMS --> INV
    OMS --> PAY
    OMS --> LOY
    OMS -. "Outbox Events" .-> KAFKA
    INV -. "inventory.updated" .-> KAFKA
    LOY -. "loyalty.points.changed" .-> KAFKA
    KAFKA --> NOTIF
    KAFKA --> ACLERP
    KAFKA --> ACLPOS
    KAFKA --> DATAHUB
    ACLPOS -. "pos.stock.delta" .-> KAFKA
    ACLERP -. "erp.sku.master" .-> KAFKA
    PAY --> FINPAY
    PAY --> COURIER
```

*Gambar 5.1 — Diagram 1: Topologi Arsitektur Solusi End-to-End Proyek OMNI (Clients → Edge → API Gateway/BFF → Domain Services → Event Bus → ACL → Legacy ERP/WMS/POS, FinPay, dan DataHub).*

---

### 5.1 Arsitektur API Modern, API Gateway, dan Pola BFF

*Application Programming Interface* (API) adalah kontrak formal yang mengikat seluruh komponen ekosistem digital. Pada proyek yang melibatkan banyak tim dan vendor—seperti PT NDS (Proyek OMNI), tim internal ERP-Refresh, tim POS-Modern, dan mitra PT FinPay Nusantara—desain API yang buruk langsung memicu keterlambatan integrasi, lonjakan *bug* produksi, hingga kerentanan keamanan serius.

#### A. Prinsip RESTful API & Pendekatan *Contract-First*

Gaya arsitektur **REST** (*Representational State Transfer*) tetap menjadi standar *de facto* untuk API publik dan antarmuka klien-server karena kesederhanaannya, dukungan *caching* HTTP bawaan, dan ekosistem perkakas yang matang. Standar desain REST tingkat senior meliputi:

1. **Penamaan Sumber Daya (*Resource Naming*) Berbasis Kata Benda Jamak & Hierarkis:** Gunakan kata benda jamak huruf kecil dengan tanda hubung (*kebab-case*), hindari kata kerja di URI. Contoh baik: `GET /v1/stores/JKT-014/inventory?sku=SKU-88210`, `POST /v1/orders`, `POST /v1/inventory/reservations`. Contoh buruk: `POST /getStockByStore` atau `GET /createNewOrder`.
2. **Semantik Metode HTTP & Sifat *Idempotency*:**
   - `GET`: Membaca data (*safe* & *idempotent* — tidak mengubah *state* server).
   - `POST`: Membuat sumber daya baru atau memicu aksi non-idempoten secara bawaan. **Kritis pada transaksi finansial & reservasi stok:** wajib menyertakan header **`Idempotency-Key`** (UUID v4 yang dibuat klien per niat transaksi) agar jika jaringan mobile pelanggan putus lalu aplikasi mengirim ulang (*retry*) `POST /v1/orders`, server mengembalikan hasil transaksi pertama tanpa membuat pesanan ganda atau memotong poin loyalty dua kali!
   - `PUT`: Mengganti sumber daya secara utuh (*idempotent*).
   - `PATCH`: Memperbarui sebagian atribut sumber daya (mis. mengubah status pesanan *Click & Collect* dari `PICKING` menjadi `READY_FOR_PICKUP`).
   - `DELETE`: Menghapus atau membatalkan sumber daya (*idempotent*).
3. **Kode Status HTTP yang Presisi:**
   - `200 OK` (sukses baca/ubah), `201 Created` (sukses buat sumber daya baru), `202 Accepted` (permintaan diterima untuk diproses asinkron via antrean).
   - `400 Bad Request` (validasi *payload* gagal), `401 Unauthorized` (token tidak valid/kedaluwarsa), `403 Forbidden` (terautentikasi tetapi tidak berwenang mengakses sumber daya tersebut), `404 Not Found`, `409 Conflict` (konflik *state*, mis. stok habis atau *Idempotency-Key* bertabrakan), `422 Unprocessable Entity` (aturan bisnis dilanggar), `429 Too Many Requests` (melewati batas *rate limit*, sertakan header `Retry-After`).
   - `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable` (termasuk saat *Circuit Breaker* terbuka), `504 Gateway Timeout`.
4. **Paginasi (*Pagination*) & Penyaringan:** Untuk 18.500 SKU atau riwayat jutaan pesanan, hindari `OFFSET` besar (mis. `OFFSET 50000`) pada SQL karena memaksa *database* memindai dan membuang puluhan ribu baris. Gunakan **Cursor-Based Pagination** (`?cursor=eyJpZCI6MTA1MH0&limit=20`) untuk performa konsisten $O(1)$ berbasis indeks.
5. **Strategi *Versioning* & *Contract-First* (OpenAPI 3.1 / Swagger):** Cantumkan versi mayor pada URI (`/v1/orders`) untuk perubahan yang memutus kompatibilitas (*breaking changes*), sedangkan penambahan field opsional dilakukan secara *backward-compatible*. Dalam pendekatan **Contract-First**, Dimas Prasetyo bersama tim POS-Modern dan PT NDS menyepakati file spesifikasi **OpenAPI 3.1 (YAML)** terlebih dahulu di awal sprint—sebelum satu baris kode pun ditulis. Dari spesifikasi tersebut, *Mock Server* otomatis dibangkitkan sehingga tim frontend Mobile/Web dan OMS dapat bekerja paralel meski API riil POS-Modern mundur 3 minggu (mitigasi risiko **R-01**).

#### B. Perbandingan Gaya Komunikasi API: REST vs GraphQL vs gRPC vs Webhook

Tidak semua jalur komunikasi cocok memakai REST. Seorang Solution Architect memilih protokol sesuai profil trafik, tipe konsumen, dan kebutuhan latensi:

| Dimensi | REST (HTTP/JSON) | GraphQL (HTTP/JSON) | gRPC (HTTP/2 + Protobuf) | Webhook (HTTP Callback) |
|---------|------------------|---------------------|--------------------------|-------------------------|
| **Model Komunikasi** | *Request–Response* berbasis *resource* URI | *Request–Response* dengan *query* fleksibel 1 *endpoint* | *Remote Procedure Call* biner (*unary* & *bidirectional streaming*) | *Event Push* satu arah dari server penyedia ke *endpoint* penerima |
| **Format & Efisiensi** | Teks JSON (mudah dibaca, *overhead* menengah) | Teks JSON (mengurangi *over-fetching* & *under-fetching*) | Biner *Protocol Buffers* (sangat ringkas, 5–10× lebih cepat dari JSON) | Teks JSON ditandatangani HMAC-SHA256 |
| **HTTP Caching** | Sangat baik (bawaan CDN & browser via `ETag` / `Cache-Control`) | Sulit pada level HTTP (umumnya memakai `POST`) | Tidak memakai *cache* HTTP standar | Tidak relevan |
| **Kompleksitas & Risiko** | Rendah–menengah; kontrak eksplisit via OpenAPI | Menengah–tinggi; rawan *N+1 query* & *query depth DoS* jika tanpa proteksi | Menengah; kurang ramah langsung ke browser tanpa gRPC-Web | Harus menangani *duplicate delivery*, verifikasi *signature*, dan *retry* |
| **Penerapan Tepat di Proyek OMNI** | **API Eksternal & Publik** (BFF, Store App, Adaptor POS, API Mitra Kurir) | Opsional di lapisan **Catalog/App Aggregation** jika tampilan Mobile & Web menuntut kombinasi data sangat dinamis *(tidak wajib di Fase 1)* | **Komunikasi Internal *East–West*** berlatensi sangat rendah antar-layanan (mis. OMS ↔ Inventory Service ↔ Loyalty Engine) | **Notifikasi Asinkron Mitra Eksternal**: callback status pembayaran dari **PT FinPay Nusantara** & pembaruan resi dari Agregator Kurir |

#### C. Peran API Gateway dan Pola *Backend for Frontend* (BFF)

Menempatkan *domain services* langsung terbuka ke internet adalah kesalahan arsitektur fatal. Di garis depan ekosistem Proyek OMNI berdiri **API Gateway** yang menjalankan fungsi *cross-cutting concerns* secara terpusat:
- **TLS Termination & Security Enforcement:** Mengakhiri koneksi HTTPS (TLS 1.3), memvalidasi format token **JWT** (*JSON Web Token*) yang diterbitkan *Identity Provider* melalui protokol **OAuth 2.0 / OpenID Connect (OIDC)**, serta menegakkan *IP allow-listing* untuk *endpoint* internal/mitra.
- **Rate Limiting & Throttling:** Membatasi permintaan per pengguna/IP (mis. 60 permintaan/menit untuk *endpoint* login atau penebusan voucher guna mencegah *brute-force* dan *bot scalper* saat Harbolnas), sekaligus menerapkan *burst quota* untuk melindungi layanan hilir.
- **Routing, Request Aggregation & Observability:** Menyisipkan `X-Correlation-ID` pada setiap permintaan masuk, mencatat metrik latensi/kode status, dan meneruskan trafik ke layanan tujuan.

Di belakang API Gateway, Proyek OMNI menerapkan pola **Backend for Frontend (BFF)**. Mengapa? Kebutuhan klien Mobile, Web, dan Tablet Toko sangat berbeda:
- **Mobile BFF:** Menggabungkan panggilan ke Catalog, Inventory, dan Loyalty dalam satu respons JSON super-ringkas (ukuran gambar terkompresi *WebP*, hanya field yang tampil di layar 6 inci) untuk menghemat kuota seluler pelanggan di luar Jawa.
- **Web BFF:** Mengirim metadata lengkap untuk *Server-Side Rendering* (SSR), *breadcrumb*, ulasan, dan optimasi SEO agar peringkat pencarian organik naik.
- **Store Ops BFF:** Dioptimalkan khusus untuk 240 tablet *Store Fulfillment App* di 120 toko dengan dukungan *delta sync* pesanan *Click & Collect*, antrean lokal *offline-tolerant*, dan pemindaian *barcode/QR* cepat.

---

### 5.2 Database Architecture, Polyglot Persistence, dan Strategi Caching

Kesalahan klasik saat memigrasi ritel konvensional ke omnichannel adalah memaksakan **satu mesin basis data relasional raksasa** menangani segalanya: katalog 18.500 SKU yang penuh variasi atribut, pencarian teks bebas dengan salah ketik (*typo*), sesi 500.000 pengguna bulanan, kunci reservasi stok berkecepatan tinggi, sekaligus transaksi akuntansi pesanan. Hasilnya hampir pasti sama: *database bottleneck* dan *downtime* saat promosi puncak.

Pendekatan modern adalah **Polyglot Persistence**—memilih teknologi penyimpanan data yang paling sesuai dengan pola baca/tulis (*access pattern*) dan jaminan konsistensi setiap domain.

```mermaid
flowchart TD
    subgraph SERVICES["Layanan Domain Proyek OMNI"]
        CATS["Catalog & Search Service"]
        INVS["Inventory & Reservation Service"]
        OMSS["OMS & Loyalty Service"]
    end
    subgraph CACHE_SEARCH["Lapisan Kecepatan Tinggi (Sub-10 ms)"]
        REDIS["Redis Cluster (In-Memory Key-Value)<br/>1) Cache Katalog & Sesi (TTL)<br/>2) Atomic Stock Lock / Counter<br/>3) Idempotency Key & Rate Limit"]
        ES["Elasticsearch / OpenSearch<br/>1) Full-Text Search 18.500 SKU<br/>2) Faceted Filter & Typo Tolerance<br/>3) Geo-Distance 120 Toko Terdekat"]
    end
    subgraph PERSIST["Lapisan Persistensi Primer & Analitik"]
        MONGO["Document DB (MongoDB / DocumentDB)<br/>Atribut Fleksibel 8 Kategori SKU<br/>& Konten Kaya Produk"]
        PG_PRI["PostgreSQL Primary (ACID)<br/>Order, Reservasi Stok, Ledger Poin<br/>& Log Persetujuan UU PDP"]
        PG_REP["PostgreSQL Read Replicas (2x)<br/>Riwayat Pesanan, Laporan Toko<br/>& Query Baca Berat"]
        S3["Object Storage (S3 / GCS)<br/>Foto SKU, Bukti Serah Terima BOPIS<br/>& Arsip Audit Enkripsi AES-256"]
    end
    CATS -->|"1. Cek Cache (Cache-Aside)"| REDIS
    CATS -->|"2. Query Pencarian & Lokasi"| ES
    CATS -->|"3. Sumber Kebenaran Katalog"| MONGO
    CATS -->|"4. Media Aset via CDN"| S3
    INVS -->|"Atomic Lock & Fast Read"| REDIS
    INVS -->|"Commit Reservasi ACID"| PG_PRI
    INVS -. "Async Index Update" .-> ES
    OMSS -->|"Cek Idempotency Key"| REDIS
    OMSS -->|"Write Transaksi ACID"| PG_PRI
    OMSS -->|"Read Riwayat & Dashboard"| PG_REP
    PG_PRI ==>|"Streaming Replication"| PG_REP
```

*Gambar 5.2 — Diagram 4: Strategi Polyglot Persistence dan Caching Proyek OMNI (Redis, Elasticsearch, MongoDB, PostgreSQL Primary/Read Replicas, dan Object Storage).*

#### A. Memilih Relational (SQL — ACID) vs NoSQL

| Kategori Basis Data | Teknologi Contoh | Jaminan & Kekuatan Inti | Kapan Dipakai di Proyek OMNI | Kapan TIDAK Dipakai |
|---------------------|------------------|-------------------------|------------------------------|---------------------|
| **Relational (RDBMS)** | PostgreSQL (Managed RDS / Cloud SQL) | Transaksi **ACID** (*Atomicity, Consistency, Isolation, Durability*), skema ketat, *foreign key*, *row-level locking*, *row partitioning* | **OMS (Orders & Order Items)**, **Inventory Reservation Ledger**, **Loyalty Point Ledger** (tidak boleh ada selisih poin atau *double-spend*), **Consent Audit UU PDP** | Pencarian teks bebas dengan *fuzzy matching* atau penyimpanan atribut produk yang berubah-ubah tiap minggu |
| **Document NoSQL** | MongoDB / AWS DocumentDB | Skema fleksibel berbasis JSON/BSON, agregasi objek bersarang (*nested document*) tanpa banyak *JOIN* | **Master Katalog 18.500 SKU** di 8 kategori *home living* (sofa punya dimensi & bahan kain; lampu punya watt & suhu warna; alat dapur punya material *food-grade*) | Transaksi akuntansi/finansial multi-entitas yang menuntut transaksi ACID ketat lintas koleksi |
| **Key-Value In-Memory** | Redis (Cluster / Memorystore) | Latensi sub-milidetik (< 2 ms), operasi atomik *single-threaded* (`DECRBY`, Lua Script), dukungan TTL otomatis | **Cache-Aside** halaman produk populer, **Distributed Lock & Atomic Stock Counter** saat *checkout*, penyimpanan **`Idempotency-Key`** (TTL 24 jam), *Rate Limiter* | Penyimpanan permanen tunggal (*system of record*) untuk data keuangan/audit jangka panjang |
| **Search Engine** | Elasticsearch / OpenSearch | *Inverted index*, *typo tolerance* (*fuzzy search*), sinonim Bahasa Indonesia ("gelas" = "mug/tumbler"), *faceted filtering*, *geo-spatial index* | **Pencarian 18.500 SKU** & **pencarian toko terdekat** (*Click & Collect*) berdasarkan koordinat GPS pelanggan terhadap 120 toko | Basis data transaksional primer (*eventually consistent*, bukan ACID) |

#### B. Skalabilitas Data: *Read Replicas*, *Partitioning*, dan *Sharding*

1. **Read Replicas:** Pada ritel omnichannel, rasio baca jauh melampaui tulis (~20:1). Dengan mengarahkan kueri baca berat (riwayat transaksi pelanggan, dasbor antrean 120 toko, ekspor laporan operasional) ke **PostgreSQL Read Replicas**, node **Primary** dapat fokus sepenuhnya pada transaksi *write* (pembuatan pesanan, reservasi stok, mutasi poin). Arsitek wajib memperhitungkan ***Replication Lag*** (jeda replikasi beberapa puluh milidetik): tepat setelah pelanggan menyelesaikan *checkout*, layar konfirmasi harus membaca dari *Primary* atau respons langsung API (*read-your-own-writes*), bukan dari *Read Replica* yang mungkin belum menerima baris baru.
2. **Partitioning (Pemartisian Vertikal/Horizontal di 1 Instance):** Tabel `orders` dan `inventory_movements` akan tumbuh jutaan baris dalam 2–3 tahun. **Range Partitioning** per bulan (`orders_2027_11`, `orders_2027_12`) menjaga indeks tetap kecil di memori RAM dan mempermudah pengarsipan (*cold archival*) data lama tanpa *table lock*.
3. **Sharding (Pemecahan ke Banyak Node Independen):** Hanya diperlukan jika volume *write* atau ukuran data melampaui batas satu *instance* vertikal terbesar (biasanya > beberapa terabita atau > puluhan ribu *write* TPS). Untuk skala SNR (18.500 SKU, 500.000 MAU, 125 TPS *burst*), **Sharding SQL TIDAK diperlukan di Fase 1**—memaksakan *sharding* terlalu dini justru menambah kompleksitas *cross-shard join* dan operasional tanpa manfaat sepadan.

#### C. Strategi *Caching* & Pencegahan *Cache Stampede*

- **Cache-Aside (*Lazy Loading*):** Aplikasi mengecek Redis terlebih dahulu. Jika *cache hit*, kembalikan dalam < 2 ms. Jika *cache miss*, baca dari basis data, tulis ke Redis dengan **TTL (*Time-To-Live*)**, lalu kembalikan ke klien. Cocok untuk detail produk dan halaman katalog.
- **Write-Through:** Setiap pembaruan data ke basis data juga langsung memperbarui Redis secara serempak. Cocok untuk angka **stok tersedia per toko–SKU** agar aplikasi tidak membaca angka kedaluwarsa.
- **Cache Invalidation & Bahaya *Cache Stampede*:** Menentukan kapan menghapus *cache* adalah salah satu masalah tersulit di ilmu komputer. Untuk stok SNR, gunakan **event-driven cache invalidation** (setiap *event* `inventory.updated` masuk, segera perbarui atau hapus kunci Redis `stock:{store_id}:{sku}` dengan *safety TTL* 60 detik). Guna mencegah ***Cache Stampede / Thundering Herd*** (ribuan pengguna menghantam basis data serentak tepat saat TTL produk promo Harbolnas habis), tambahkan **TTL Jitter** (mis. 300 detik + acak 0–60 detik) dan mekanisme *single-flight / mutex lock* saat mengisi ulang *cache*.

#### D. CAP Theorem, PACELC, dan Konsistensi Realistis di 120 Toko

**Teorema CAP** (Eric Brewer) menyatakan bahwa dalam sistem terdistribusi, ketika terjadi **Partition Tolerance (P)**—putusnya koneksi jaringan antar-node—sistem hanya dapat memilih salah satu dari dua jaminan: **Consistency (C)** (setiap pembacaan mengembalikan data tulis terbaru atau galat) atau **Availability (A)** (setiap permintaan mendapat respons non-galat, meski datanya mungkin sedikit usang).

Di dunia nyata jaringan 120 toko SNR lintas 24 kota (termasuk Sumatra, Kalimantan, Sulawesi, dan Bali–Nusra), **partisi jaringan (P) pasti terjadi**. Oleh karena itu, arsitek harus memilih di titik mana sistem bersifat **CP** dan di titik mana **AP (*Eventual Consistency*)**:
- **CP (*Strong Consistency*):** Wajib untuk **reservasi stok saat *checkout* online**, **transaksi pembayaran**, dan **pemotongan saldo poin loyalty** (menggunakan transaksi ACID PostgreSQL + kunci atomik Redis). Lebih baik menolak *checkout* sementara daripada menjual barang fiktif (*overselling*) atau membuat saldo poin minus.
- **AP (*Eventual Consistency*):** Tepat untuk **tampilan angka stok di halaman katalog** (jeda ≤ 60 detik dapat diterima), **penjualan kasir fisik POS di toko saat internet toko putus** (kasir fisik tidak boleh berhenti melayani antrean pelanggan di toko hanya karena internet ke Jakarta putus! Transaksi POS dicatat lokal di toko dan disinkronkan secara asinkron saat koneksi pulih), serta **pengiriman data analitik ke DataHub**.

---

### 5.3 Gaya Arsitektur Aplikasi, DDD Bounded Contexts, dan Strangler Fig

Salah satu debat paling sengit—dan paling mahal jika salah diputuskan—dalam proyek modernisasi korporasi adalah memilih antara **Monolith**, **Modular Monolith**, dan **Microservices**.

| Dimensi | Traditional Monolith (*Big Ball of Mud*) | Modular Monolith | Right-Sized Microservices / Domain Services (5–8 layanan) | Fine-Grained Microservices (20+ layanan) |
|---------|------------------------------------------|------------------|-----------------------------------------------------------|------------------------------------------|
| **Deployment & Scaling** | Satu artefak; seluruh aplikasi di-*scale* bersama | Satu artefak *deploy*, batas modul internal tegas | Tiap domain krusial bisa di-*deploy* & di-*scale* mandiri (mis. Search & Inventory) | Sangat granular; puluhan *pipeline* CI/CD & kontrak |
| **Isolasi Data** | Satu skema DB bercampur (*tight coupling*) | Satu DB fisik, tetapi skema/tabel terisolasi per modul | *Database-per-service* (isolasi logis/fisik per domain) | Puluhan DB terpisah; transaksi terdistribusi sangat kompleks |
| **Latensi & Debugging** | Panggilan memori lokal (< 1 ms); sangat mudah di-*debug* | Panggilan memori lokal; mudah di-*refactor* ke layanan terpisah kelak | Panggilan jaringan/event antar-domain; butuh *Distributed Tracing* | Latensi berantai tinggi; *debugging* lintas 20 layanan sangat berat |
| **Kebutuhan Kematangan DevOps & Tim** | Rendah (tim kecil 3–10 orang) | Rendah–Menengah (tim 8–20 orang) | Menengah–Tinggi (tim 15–30 orang dengan CI/CD & K8s terkelola) | Sangat Tinggi (> 50–100 engineer, *platform team* khusus, *service mesh*) |
| **Risiko Utama** | Sulit dirawat jangka panjang; *blast radius* 100% | Disiplin batas modul bisa jebol jika tanpa aturan arsitektur | Overhead *eventual consistency* & orkestrasi *Saga* | **Distributed Monolith**, jadwal molor, biaya cloud & operasional membengkak |

#### A. Hukum Conway (*Conway's Law*) dan *Domain-Driven Design* (DDD)

Melvin Conway mengamati bahwa *"organisasi yang merancang sistem akan menghasilkan desain yang strukturnya menyalin struktur komunikasi organisasi tersebut."* Pada Proyek OMNI, tim pengembangan PT NDS terdiri atas **18 personel** (sekitar 10–12 *software engineer*, sisanya QA, DevOps, PM/BA), dibantu tim kecil IT internal SNR. Jika kita memaksakan **25 microservices** pada 12 *engineer*, artinya setiap *engineer* harus mengelola 2 layanan terpisah lengkap dengan repositori, *pipeline* CI/CD, skema basis data, *alerting*, dan kompatibilitas API—resep pasti menuju ***Premature Microservices*** dan keterlambatan jadwal.

Pendekatan *Domain-Driven Design* (DDD) memecah sistem berdasarkan **Bounded Context**—batas semantik yang jelas di mana setiap istilah bisnis (misalnya "Produk", "Stok", atau "Pesanan") memiliki definisi dan kepemilikan data tunggal:
1. **Catalog & Search Context:** Mengelola informasi deskriptif 18.500 SKU, kategori, harga dasar, dan pencarian berbasis lokasi.
2. **Inventory & Reservation Context:** Mengelola *Available-to-Promise* (ATP) per toko/DC, *safety stock*, reservasi sementara (*hold* 15 menit saat *checkout*), serta konsolidasi sinkronisasi stok dari ERP/WMS/POS.
3. **Order Management & BOPIS Context (OMS):** Mengelola siklus hidup pesanan, orkestrasi *Saga* pembayaran–stok–loyalty, serta alur kerja *Click & Collect* (SLA ≤ 2 jam di 120 toko).
4. **Digital Loyalty Context:** Mengelola profil anggota terverifikasi, perhitungan poin, tingkat *Silver/Gold/Platinum*, dan validasi kupon QR anti-duplikasi.
5. **Payment & Fulfillment Integration Context:** Mengisolasi integrasi eksternal ke PT FinPay Nusantara (PCI-DSS) dan agregator kurir.
6. **Notification & Customer Consent Context:** Mengelola pengiriman notifikasi multi-kanal serta catatan persetujuan (*consent*) dan permintaan hak subjek data UU PDP.

#### B. Memodernisasi Sistem *Legacy* dengan *Strangler Fig Pattern* & *Anti-Corruption Layer*

PT SNR tidak mungkin melakukan pendekatan ***Big Bang Cutover*** (mematikan ERP dan POS lama di 120 toko lalu menyalakan sistem baru serentak dalam satu malam)—risiko melumpuhkan pendapatan Rp 1,85 triliun/tahun terlalu besar. Sebagai gantinya, proyek menerapkan **Strangler Fig Pattern** (Martin Fowler), terinspirasi dari pohon ara pencekik yang tumbuh bertahap di sekeliling pohon inang hingga akhirnya menggantikan fungsinya secara aman:

1. **Intercept:** Semua kanal baru (Mobile, Web, Store Fulfillment App) berkomunikasi hanya dengan OMS & API Gateway baru, tidak pernah menembak basis data ERP/POS lama secara langsung.
2. **Translate via Anti-Corruption Layer (ACL):** Lapisan ACL menerjemahkan struktur data usang ERP/POS lama (misalnya kode gudang numerik 4 digit, format file *fixed-width*, atau skema tabel peninggalan 2012) menjadi model domain bersih Proyek OMNI (`store_code: "JKT-014"`, `sku: "SKU-88210"`, standar ISO-8601).
3. **Migrate Incrementally (Wave Rollout):** Dimulai dari Pilot 10 toko Jabodetabek (Gate 3), dilanjutkan Gelombang 1 (30 toko), Gelombang 2 (40 toko), hingga Gelombang 3 (40 toko). Ketika proyek **POS-Modern** dan **ERP-Refresh** menaikkan versi API baru di tiap gelombang, hanya adaptor di dalam ACL yang diganti—inti OMS tidak perlu diubah sama sekali!

```mermaid
flowchart LR
    subgraph NEW["Platform Modern Proyek OMNI (Model Domain Bersih)"]
        OMS["OMS & Inventory Service<br/>(Schema Modern JSON/ISO-8601)"]
        LOY["Digital Loyalty Service<br/>(QR Voucher & Poin Real-Time)"]
    end
    subgraph STRANGLER["Routing & Anti-Corruption Layer (ACL)"]
        ROUTER["Strangler Router / Feature Flag<br/>Migrasi Bertahap per Gelombang Toko<br/>(Pilot 10 → G1 30 → G2 40 → G3 40)"]
        ACLPOS["ACL POS Adapter<br/>Terjemah Skema Lama ↔ Baru<br/>& Queue Buffer Offline"]
        ACLERP["ACL ERP & WMS Adapter<br/>Terjemah Master SKU & Stok 3 DC"]
    end
    subgraph LEGACY["Ekosistem Eksisting & Proyek Paralel SNR"]
        POS_OLD["POS Legacy (Batch 00.00 WIB)<br/>Toko Belum Dimigrasi"]
        POS_NEW["POS-Modern API (PRJ-03)<br/>Toko Sudah Dimigrasi (Sync ≤ 60 dtk)"]
        ERP_OLD["ERP Legacy & WMS 3 DC<br/>(Cikarang, Surabaya, Medan)"]
        ERP_NEW["ERP-Refresh API (PRJ-02)<br/>Master SKU & Stok Pusat Baru"]
    end
    OMS --> ROUTER
    LOY --> ROUTER
    ROUTER -->|"Fase Awal / Fallback"| ACLPOS
    ROUTER -->|"Toko Gelombang Baru"| POS_NEW
    ACLPOS -->|"Polling / Delta Sync"| POS_OLD
    ACLPOS -. "Transisi Adaptor" .-> POS_NEW
    OMS --> ACLERP
    ACLERP -->|"Mode Transisi"| ERP_OLD
    ACLERP -->|"Target Akhir 2027"| ERP_NEW
```

*Gambar 5.3 — Diagram 7: Pola Strangler Fig dan Anti-Corruption Layer (ACL) yang Memungkinkan Migrasi Bertahap 120 Toko dan Dekoupling dari ERP-Refresh serta POS-Modern.*

---

### 5.4 Pola Integrasi Sistem (*Enterprise Integration Patterns*) dan Ketahanan

Integrasi adalah titik paling rapuh dalam arsitektur korporasi. Berdasarkan catatan *Enterprise Integration Patterns* (Gregor Hohpe & Bobby Woolf), arsitek wajib memisahkan jalur **sinkron** dari jalur **asinkron**, lalu membentengi setiap batas jaringan dengan pola ketahanan (*resilience patterns*).

#### A. Sinkron vs Asinkron (*Event-Driven Architecture*), *Transactional Outbox*, dan *DLQ*

Pada integrasi **sinkron** (REST/gRPC), pemanggil menunggu respons langsung sebelum lanjut. Ini diperlukan saat pelanggan butuh kepastian seketika (contoh: cek apakah stok toko tersedia saat klik tombol *Bayar*, atau validasi kode QR voucher di kasir). Namun, jika seluruh proses pasca-pesanan—mengirim notifikasi WhatsApp, memperbarui indeks Elasticsearch, mengirim data ke DataHub, dan mencatat jurnal ke ERP—dirangkai secara sinkron, maka perlambatan 10 detik di ERP akan membuat layar *checkout* pelanggan macet (*cascading failure*).

Pada **Event-Driven Architecture (EDA)** asinkron, layanan produsen menerbitkan *event* fakta bisnis yang telah terjadi (mis. `order.created`, `inventory.updated`, `payment.settled`) ke **Message Broker** (Apache Kafka atau Google Cloud Pub/Sub). Banyak konsumen (*Consumer Groups*) dapat membaca *event* yang sama secara independen dengan kecepatan masing-masing (*loose coupling*).

Dua mekanisme wajib pada produksi EDA tingkat senior:
1. **Transactional Outbox Pattern (Solusi *Dual-Write Problem*):** Bagaimana menjamin bahwa saat pesanan tersimpan di PostgreSQL, *event* `order.created` pasti terkirim ke Kafka—dan tidak hilang jika aplikasi *crash* tepat di antara simpan DB dan *publish* Kafka? Caranya: simpan data pesanan **dan** baris *event* ke tabel `outbox_events` di **dalam satu transaksi ACID PostgreSQL yang sama**. Selanjutnya, proses *relay* (atau *Change Data Capture* / Debezium) membaca tabel `outbox_events` dan mengirimkannya ke Kafka dengan jaminan *at-least-once delivery*. Karena pesan bisa terkirim lebih dari sekali saat *retry*, setiap konsumen wajib bersifat **Idempotent Consumer** (menyimpan `event_id` yang sudah diproses).
2. **Dead Letter Queue (DLQ):** Jika konsumen gagal memproses suatu *event* berulang kali (misalnya *payload* korup dari adaptor POS atau aturan validasi tidak cocok) setelah batas *retry* (mis. 5 kali), pesan tidak boleh memblokir seluruh antrean (*poison pill*) dan tidak boleh dibuang diam-diam. Pesan dipindahkan otomatis ke **DLQ** yang memicu *alert* ke tim operasi untuk diinvestigasi dan diputar ulang (*replay*) setelah perbaikan.

```mermaid
flowchart LR
    subgraph SYNC["Pola 1: Rantai Sinkron (Rentan Cascading Failure)"]
        direction LR
        C1["Pelanggan<br/>Checkout"] -->|"REST (Tunggu)"| O1["OMS"]
        O1 -->|"REST (Tunggu)"| E1["ERP Legacy<br/>(Lambat/Down)"]
        E1 -->|"REST (Tunggu)"| N1["Email/WA<br/>Notifikasi"]
        N1 -. "Timeout 30 dtk!<br/>Checkout Gagal Total" .-> C1
    end

    subgraph ASYNC["Pola 2: Event-Driven + Transactional Outbox + DLQ (Direkomendasikan)"]
        direction LR
        C2["Pelanggan<br/>Checkout"] -->|"REST Cepat (≤ 400 ms)"| O2["OMS Service"]
        O2 -->|"1 Transaksi ACID:<br/>orders + outbox_events"| DB2[("PostgreSQL<br/>OMS DB")]
        DB2 -->|"CDC / Outbox Relay"| K2["Event Bus<br/>(Kafka / PubSub)"]
        K2 -->|"Consumer Group A"| W1["ACL ERP/WMS<br/>(Idempotent)"]
        K2 -->|"Consumer Group B"| W2["Notification Svc<br/>(Push/WA/Email)"]
        K2 -->|"Consumer Group C"| W3["Proyek DataHub<br/>(Analitik)"]
        W1 -->|"Gagal 5x Retry<br/>(Poison Pill)"| DLQ["Dead Letter Queue (DLQ)<br/>Alert & Manual Replay"]
    end
```

*Gambar 5.4 — Diagram 2: Perbandingan Integrasi Sinkron yang Rentan Efek Domino versus Arsitektur Event-Driven dengan Transactional Outbox dan Dead Letter Queue (DLQ).*

#### B. Pola Ketahanan: *Circuit Breaker* & *Retry with Exponential Backoff + Jitter*

Ketika koneksi ke ERP *legacy* atau 15 toko di luar Jawa mengalami gangguan, aplikasi yang terus-menerus menembakkan *retry* setiap 100 ms justru memperparah gangguan (*Retry Storm / Self-Inflicted DDoS*). Solusinya adalah kombinasi dua pola:
1. **Retry with Exponential Backoff & Jitter:** Hanya lakukan *retry* untuk kesalahan sementara (*transient error* seperti `502/503/504` atau *network timeout*, **bukan** `400/401/409`). Jeda antar-percobaan digandakan secara eksponensial (mis. 1 dtk → 2 dtk → 4 dtk) ditambah angka acak (*jitter*, mis. ±30%) agar ratusan klien tidak menembak ulang pada milidetik yang persis sama.
2. **Circuit Breaker Pattern:** Bertindak persis seperti sekring listrik rumah. Memiliki tiga status:
   - **Closed (Normal):** Trafik mengalir normal sambil menghitung rasio kegagalan dalam jendela waktu (*sliding window*).
   - **Open (Terputus/Proteksi):** Ketika kegagalan melampaui ambang batas (mis. ≥ 50% gagal dari 20 permintaan terakhir atau *timeout* > 3 detik berturut-turut), sekring "terbuka". Seluruh panggilan berikutnya langsung ditolak seketika (*fail fast*) atau diarahkan ke **Fallback** (mis. membaca *snapshot* stok terakhir dari Redis dengan penanda *"stok sedang diperbarui"* atau memasukkan sinkronisasi POS ke antrean asinkron) tanpa membuang *thread* menunggu *timeout*.
   - **Half-Open (Uji Pemulihan):** Setelah masa tunggu (*cooldown*, mis. 30 detik), sekring meloloskan sejumlah kecil permintaan uji coba (mis. 3 permintaan). Jika semua sukses, sekring kembali ke **Closed**; jika gagal, kembali ke **Open**.

```mermaid
stateDiagram-v2
    [*] --> Closed
    Closed: Closed (Operasi Normal)<br/>Permintaan diteruskan ke ERP/POS<br/>Hitung rasio error pada sliding window
    Open: Open (Proteksi Aktif / Fail-Fast)<br/>Hentikan panggilan langsung ke target<br/>Jalankan Fallback (Cache Redis / Antrean Asinkron)
    HalfOpen: Half-Open (Uji Pemulihan Terbatas)<br/>Loloskan 3 permintaan probe<br/>untuk cek kesehatan ERP/POS
    Closed --> Open: Kegagalan ≥ 50% (min 20 req)<br/>atau timeout lebih dari 3 dtk berturut-turut
    Open --> HalfOpen: Cooldown timer habis (30 detik)
    HalfOpen --> Closed: 3 probe beruntun SUKSES<br/>(Reset counter error)
    HalfOpen --> Open: ≥ 1 probe GAGAL / timeout<br/>(Perpanjang cooldown)
```

*Gambar 5.5 — Diagram 5: State Machine Pola Circuit Breaker (Closed → Open → Half-Open) untuk Melindungi OMS dari Gangguan ERP Legacy atau Koneksi Toko Tidak Stabil.*

#### C. Transaksi Terdistribusi: *Saga Pattern* (*Choreography* vs *Orchestration*)

Di arsitektur layanan terpisah, kita tidak dapat memakai *Two-Phase Commit* (2PC) lintas *database* dan *Payment Gateway* eksternal karena 2PC mengunci sumber daya terlalu lama dan hancur performanya di 2.500 TPM. Penggantinya adalah **Saga Pattern**: memecah satu transaksi bisnis panjang menjadi rangkaian transaksi lokal, di mana setiap langkah memiliki **Compensating Transaction** (transaksi pembalik secara semantik) apabila langkah selanjutnya gagal.

- **Saga Choreography (Tanpa Koordinator Pusat):** Tiap layanan mendengarkan *event* dan memicu langkah berikutnya sendiri. Cocok untuk alur sangat sederhana (2–3 layanan), tetapi menjadi mimpi buruk dilacak (*cyclic dependency* dan alur tersembunyi) jika melibatkan 4–5 layanan dengan banyak cabang pengecualian.
- **Saga Orchestration (Dengan Koordinator Eksplisit):** Satu layanan pusat—di Proyek OMNI yakni **OMS Orchestrator**—mengatur urutan langkah, menyimpan *state machine* pesanan, memanggil layanan terkait, dan menjalankan *compensating transaction* secara terstruktur jika terjadi kegagalan (misalnya pembayaran FinPay gagal/kedaluwarsa atau staf toko melaporkan barang *Click & Collect* ternyata cacat fisik di rak).

```mermaid
sequenceDiagram
    autonumber
    actor Cust as Pelanggan (Mobile App)
    participant OMS as OMS Orchestrator (Saga)
    participant INV as Inventory Service
    participant LOY as Digital Loyalty Service
    participant PAY as Payment Adapter (FinPay)
    participant STO as Store Fulfillment App

    Cust->>OMS: POST /v1/orders (Click & Collect, Idempotency-Key, Redeem 500 Poin)
    activate OMS
    OMS->>OMS: Simpan Order (Status: PENDING_RESERVATION)
    OMS->>INV: Reserve Stock (SKU-88210, Store: JKT-014, TTL 15 mnt)
    INV-->>OMS: 201 Reserved (reservation_id: RSV-901)
    OMS->>LOY: Lock & Deduct 500 Poin (Order: ORD-2027-001)
    LOY-->>OMS: 200 Points Locked (ledger_id: LGR-442)
    OMS->>PAY: Create Payment Session (QRIS/VA via FinPay)
    PAY-->>OMS: 201 Payment Pending (payment_url)
    OMS-->>Cust: 201 Order Created (Menunggu Pembayaran 15 mnt)
    alt Skenario A: Pembayaran Gagal / Kedaluwarsa (Webhook FinPay)
        PAY-->>OMS: Webhook: payment.failed / payment.expired
        Note over OMS,LOY: Jalankan Compensating Transactions (Rollback Semantik)
        OMS->>LOY: Compensate: Refund 500 Poin (ledger_id: LGR-442)
        LOY-->>OMS: 200 Points Restored
        OMS->>INV: Compensate: Release Stock (reservation_id: RSV-901)
        INV-->>OMS: 200 Stock Released (Publish inventory.updated)
        OMS->>OMS: Update Order (Status: CANCELLED_PAYMENT_FAILED)
        OMS-->>Cust: Push Notif: Pesanan dibatalkan, poin & kuota dikembalikan
    else Skenario B: Pembayaran Sukses, namun Fisik Barang di Toko Cacat/Kosong
        PAY-->>OMS: Webhook: payment.settled (Signed HMAC)
        OMS->>STO: Push Picking Task (SLA ≤ 2 Jam)
        STO-->>OMS: Report Exception: Barang Cacat / Selisih Fisik (Short-Pick)
        Note over OMS,PAY: Jalankan Compensating Transactions Penuh
        OMS->>PAY: Compensate: Trigger Auto-Refund ke FinPay
        PAY-->>OMS: 202 Refund Queued
        OMS->>LOY: Compensate: Refund 500 Poin
        OMS->>INV: Compensate: Adjust Stock = 0 & Flag Audit Opname Toko
        OMS->>OMS: Update Order (Status: CANCELLED_STORE_SHORTAGE)
        OMS-->>Cust: Push Notif: Refund otomatis + Voucher kompensasi / opsi pindah toko
    end
    deactivate OMS
```

*Gambar 5.6 — Diagram 3: Alur Saga Orchestration dan Compensating Transaction pada Pesanan Click & Collect Proyek OMNI saat Pembayaran Gagal atau Stok Fisik Toko Tidak Tersedia.*

---

### 5.5 Cloud Fundamentals, High Availability, Disaster Recovery, dan FinOps

#### A. Model Layanan Cloud (IaaS vs PaaS vs SaaS) & Kontainerisasi

Memilih lapisan abstraksi *cloud* menentukan seberapa besar energi tim IT internal SNR habis untuk mengurus server ketimbang menghasilkan nilai bisnis:
- **IaaS (*Infrastructure as a Service*):** Sewa mesin virtual (VM), jaringan, dan penyimpanan mentah (mis. AWS EC2 / GCP Compute Engine). Fleksibel, tetapi tim SNR menanggung penuh *OS patching*, *failover* manual, dan pengerasan sistem.
- **PaaS / Managed Services (*Platform as a Service*):** Penyedia *cloud* mengelola sistem operasi, *patching*, replikasi, dan *backup* otomatis (mis. Managed Kubernetes **EKS/GKE**, Managed PostgreSQL **RDS/Cloud SQL Multi-AZ**, Managed Redis, Managed Kafka/PubSub). **Pilihan paling rasional bagi SNR** agar tim DevOps ramping bisa fokus ke arsitektur aplikasi.
- **SaaS (*Software as a Service*):** Perangkat lunak siap pakai (mis. *Payment Gateway* FinPay, layanan *Push Notification*, SaaS Observability/SIEM). Mengurangi *time-to-market* menjelang tenggat 26 November 2027.

#### B. High Availability (Multi-AZ) vs Disaster Recovery (RPO & RTO)

Banyak tim proyek—bahkan level manajer—keliru menyamakan **High Availability (HA)** dengan **Disaster Recovery (DR)**.
- **High Availability (HA — Multi-AZ):** Melindungi sistem dari kegagalan lokal (server rusak, rak mati, putusnya listrik/jaringan di satu pusat data) dengan menempatkan beban kerja secara aktif di **minimal 2–3 Availability Zone (AZ)** terpisah dalam **satu Region Jakarta** (AWS `ap-southeast-3` atau GCP `asia-southeast2`). *Failover* terjadi otomatis dalam hitungan detik (< 60 detik) tanpa kehilangan data (*synchronous replication*).
- **Disaster Recovery (DR):** Melindungi kelangsungan bisnis dari bencana berskala besar (kerusakan total satu wilayah, kesalahan konfigurasi massal yang menghapus basis data produksi, atau serangan *ransomware*). Dua parameter wajib yang ditentukan bersama Sponsor (Ratna Kusuma) dan CTO (Irwan Pratama):
  - **RPO (*Recovery Point Objective*):** Batas toleransi **maksimum data yang boleh hilang** diukur dalam waktu (seberapa sering *backup/replikasi* dilakukan).
  - **RTO (*Recovery Time Objective*):** Batas toleransi **maksimum waktu pemulihan** sampai sistem kembali melayani transaksi.

| Strategi DR | Perkiraan RPO | Perkiraan RTO | Rasio Biaya Cloud | Kapan Tepat Dipilih? |
|-------------|---------------|---------------|-------------------|----------------------|
| **1. Backup & Restore** | 4–24 jam | 6–24 jam | 1,0× (terendah) | Sistem internal non-kritis, pelaporan *batch* |
| **2. Pilot Light** | 5–15 menit | 30–90 menit | ~1,15–1,25× | Aplikasi bisnis penting dengan anggaran sangat ketat (DB direplikasi hidup, *compute* dimatikan sampai bencana) |
| **3. Warm Standby** | **≤ 5 menit** | **≤ 30 menit** | **~1,30–1,45×** | **Target optimal Proyek OMNI**: versi skala kecil dari layanan inti menyala di lokasi/zona terisolasi + *immutable backup*, tinggal *scale-up* otomatis saat bencana |
| **4. Multi-Site Active-Active** | ~0 detik (*near-zero*) | < 1 menit | **2,5×–3,2×** | Sistem perbankan inti / bursa efek dengan SLA ≥ 99,99% dan anggaran tidak terbatas |

```mermaid
flowchart TD
    DNS["Global DNS & Cloud WAF / CDN<br/>Health Check Otomatis + TLS 1.3"]
    subgraph REGION_JKT["Primary Cloud Region: Jakarta (AWS ap-southeast-3 / GCP asia-southeast2)"]
        LB["Multi-AZ Application Load Balancer<br/>Auto-Scaling Target: 2.500 TPM / 125 TPS Burst"]
        subgraph AZ1["Availability Zone A (Active)"]
            K8S1["Managed K8s Worker Nodes<br/>API GW, BFF, OMS, Inv, Loyalty<br/>(HPA Auto-Scale 3..20 Pod)"]
            PG1[("PostgreSQL Primary<br/>(ACID Write)")]
            RED1[("Redis Primary")]
        end
        subgraph AZ2["Availability Zone B (Active)"]
            K8S2["Managed K8s Worker Nodes<br/>API GW, BFF, OMS, Inv, Loyalty<br/>(HPA Auto-Scale 3..20 Pod)"]
            PG2[("PostgreSQL Synchronous Standby<br/>+ Read Replica")]
            RED2[("Redis Replica")]
        end
        subgraph AZ3["Availability Zone C (Quorum & DR Ready)"]
            KFK["Event Bus Cluster<br/>3-AZ Replicated Brokers"]
            ES3["Elasticsearch 3-Node<br/>Cross-AZ Shards"]
            IMM["Immutable Encrypted Backups<br/>PITR 5-Menit + Object Lock<br/>(Anti-Ransomware)"]
        end
    end
    subgraph DR_STANDBY["DR Warm Standby & Isolated Recovery Account (Region Domestik / Cross-AZ Isolated)"]
        DR_DB[("Async Replica / Snapshot<br/>RPO ≤ 5 Menit")]
        DR_APP["IaC Terraform + Warm Core Pods<br/>Scale-Up Otomatis: RTO ≤ 30 Menit"]
    end
    DNS --> LB
    LB --> K8S1
    LB --> K8S2
    K8S1 --> PG1
    K8S2 --> PG1
    K8S1 --> RED1
    K8S2 --> RED2
    PG1 ==>|"Sync Replication (RPO=0 HA)"| PG2
    RED1 ==>|"Replication"| RED2
    K8S1 --> KFK
    K8S2 --> KFK
    K8S1 --> ES3
    PG1 -. "Continuous WAL Archive" .-> IMM
    PG1 -. "Encrypted Async Stream" .-> DR_DB
    IMM -. "Restore Verification Bulanan" .-> DR_APP
```

*Gambar 5.7 — Diagram 6: Topologi Cloud High Availability Multi-AZ Region Jakarta dan Strategi Disaster Recovery Warm Standby (RPO ≤ 5 Menit, RTO ≤ 30 Menit) Proyek OMNI.*

#### C. Auto-Scaling & Disiplin *FinOps* (Mencegah *Cloud Bill Shock*)

Beban e-commerce ritel sangat fluktuatif: pukul 03.00 WIB trafik hampir nol, hari kerja biasa ±150–400 TPM, sedangkan malam Harbolnas 12.12 melonjak hingga **2.500 TPM (125 TPS *burst*)**. Memesan server statis berkapasitas 2.500 TPM selama 24 jam × 365 hari akan menghancurkan anggaran **CB-03 Rp 1,15 M**.

Solusinya adalah **Horizontal Auto-Scaling** (Kubernetes HPA berdasarkan CPU/memori serta *custom metric* kedalaman antrean Kafka/RPS + *Predictive Scheduled Scaling* 2 jam sebelum promo besar dimulai) dipadukan dengan lima disiplin **FinOps**:
1. **Right-Sizing & Committed Use / Savings Plan:** Jalankan kapasitas dasar (*baseline load*) dengan diskon komitmen 1 tahun (hemat 25–35%), sementara lonjakan Harbolnas diserap node *on-demand/spot* sementara.
2. **Jadwal Mati Otomatis Non-Produksi:** Lingkungan `Dev` dan `Staging` dimatikan otomatis di luar jam kerja (pukul 20.00–07.00 WIB & akhir pekan) → memangkas biaya non-produksi hingga **±60%**.
3. **Storage Lifecycle Tiering:** Pindahkan arsip log dan foto bukti serah terima *Click & Collect* berusia > 90 hari ke kelas penyimpanan dingin (*Cold/Archive Storage*) yang biayanya 70–85% lebih murah.
4. **Cost Allocation Tagging:** Wajibkan *tag* `project=omni`, `env=prod/stg/dev`, `service=oms/inv/cat` di seluruh skrip *Infrastructure as Code* (Terraform) agar CFO **Budi Santoso** dan CTO dapat memantau *burn rate* bulanan per domain.
5. **Budget Alerts Otomatis:** Pasang peringatan pada ambang 60%, 80%, dan 95% dari kuota bulanan cloud sehingga lonjakan tak terduga (mis. *infinite retry loop* atau kebocoran egress data) terdeteksi dalam hitungan jam, bukan saat tagihan akhir bulan datang.

---

### 5.6 Keamanan *Defense-in-Depth*, Kepatuhan Regulasi, dan Observability

Di Proyek OMNI, **Rina Kartika** (Head of Legal, Compliance & InfoSec) memegang **veto power** penuh untuk menunda *Go-Live* apabila kepatuhan **UU PDP No. 27/2022**, standar **PCI-DSS**, atau hasil *Penetration Testing* independen masih menyisakan temuan *Critical/High*. Keamanan tidak boleh ditempelkan menjelang UAT (*bolt-on*), melainkan ditanam sejak rancangan awal (*Security by Design* & *Defense-in-Depth* — pertahanan berlapis).

1. **Enkripsi Menyeluruh (*In-Transit* & *At-Rest*):**
   - *In-Transit:* Wajib **TLS 1.3** pada seluruh trafik publik (Mobile/Web/POS → Edge/API Gateway) dan **mTLS** (*mutual TLS*) antar-layanan internal di dalam klaster.
   - *At-Rest:* Seluruh basis data PostgreSQL, MongoDB, Elasticsearch, broker Kafka, dan Object Storage dienkripsi dengan **AES-256** menggunakan kunci yang dikelola di **Cloud KMS** (*Key Management Service*) dengan rotasi otomatis. Data pribadi sensitif (*PII*: nomor ponsel, email, alamat, tanggal lahir anggota loyalty) menerapkan **Envelope Encryption / Field-Level Encryption** dan disamarkan (*masking*) di seluruh log aplikasi.
2. **Reduksi Lingkup PCI-DSS via Tokenisasi (PT FinPay Nusantara):**
   - Menyimpan nomor kartu kredit (*PAN*) dan CVV di server sendiri mewajibkan audit PCI-DSS Level 1 yang sangat mahal dan rumit. Arsitektur Proyek OMNI menerapkan **Hosted Fields / SDK Tokenisasi** milik **PT FinPay Nusantara**: data kartu langsung dikirim dari perangkat pelanggan ke server FinPay, lalu FinPay hanya mengembalikan **token acak** dan status pembayaran via *webhook* bertanda tangan HMAC-SHA256 ke OMS SNR. Dengan cara ini, server SNR tidak pernah menyentuh data kartu sensitif sehingga lingkup kepatuhan menyusut drastis ke level *SAQ-A*.
3. **Kepatuhan Teknis UU PDP No. 27/2022:**
   - **Residensi Data:** Seluruh data primer dan replika DR berada di wilayah hukum Indonesia (**Cloud Region Jakarta**).
   - **Manajemen Persetujuan (*Consent Management*):** Tabel `customer_consents` mencatat versi kebijakan privasi, jenis persetujuan (*purpose limitation*: transaksi vs pemasaran), stempel waktu, dan kanal persetujuan secara tak terubah (*immutable*).
   - **Hak Subjek Data:** Menyediakan API & alur otomatis bagi pelanggan untuk mengunduh data (*Data Portability*), memperbaiki data, mencabut persetujuan promosi, serta **penghapusan/anonimisasi PII** (*Right to Erasure*) tanpa merusak integritas catatan pembukuan transaksi fiskal (memisahkan tabel identitas PII dari tabel fakta pesanan melalui `customer_uuid` — *crypto-shredding / pseudonymization*).
   - **Kesiapan Insiden 3×24 Jam:** Integrasi SIEM dan *audit trail* untuk mendeteksi akses tak sah dan memenuhi kewajiban pemberitahuan kegagalan pelindungan data maksimal **3×24 jam** sesuai Pasal 46 UU PDP.
4. **Mitigasi OWASP API Security Top 10 (Prioritas Proyek OMNI):**
   - **API1 — BOLA (*Broken Object Level Authorization*):** Pelanggan A mencoba mengakses `GET /v1/orders/ORD-999` milik Pelanggan B. *Mitigasi:* validasi kepemilikan `order.customer_id == jwt.sub` di setiap lapisan layanan, gunakan UUID acak (bukan angka berurutan `1001, 1002`).
   - **API4 — Unrestricted Resource Consumption:** Serangan kueri pencarian berat atau *scraping* stok 120 toko. *Mitigasi:* *Rate limiting* di API Gateway, batas maksimum `limit=50` pada paginasi, dan proteksi WAF bot.
   - **API5 — BFLA (*Broken Function Level Authorization*):** Akun pelanggan mencoba memanggil *endpoint* staf toko `PATCH /v1/store/orders/{id}/ready`. *Mitigasi:* **RBAC** ketat berbasis *scopes/roles* di JWT (`role: STORE_STAFF`, *store_id binding*).
   - **API6 — Unrestricted Access to Sensitive Business Flows:** Bot memborong reservasi stok promo atau menebus kode voucher berulang kali (*inventory hoarding / coupon abuse*). *Mitigasi:* batas reservasi aktif per pengguna, durasi *hold* 15 menit, dan penguncian atomik kupon.
5. **Observability (3 Pilar Terpadu):**
   - **Metrics (Metrik Kuantitatif):** Memantau *Four Golden Signals* (SRE Google) — **Latency** (p50/p95/p99), **Traffic** (RPS/TPM), **Errors** (rasio 4xx/5xx), dan **Saturation** (CPU, memori, *connection pool*, *Kafka consumer lag*) via Prometheus/Grafana atau Cloud Monitoring.
   - **Structured Logs (Log Terstruktur):** Format JSON seragam yang wajib memuat `timestamp`, `service`, `level`, `correlation_id`, dan `trace_id`—dengan **filter otomatis PII scrubber** agar nomor HP, email, dan token JWT tidak pernah bocor ke log.
   - **Distributed Tracing:** Menggunakan standar **OpenTelemetry** untuk melacak satu transaksi dari klik pelanggan di Mobile App → API Gateway → BFF → OMS → Redis/PostgreSQL → Kafka → ACL POS. Ketika latensi melonjak di atas 2 detik, tim langsung melihat *span* mana yang menjadi biang keladi dalam hitungan menit, bukan saling menyalahkan antar-vendor.

---

### 5.7 Architecture Decision Record (ADR) dan Kesalahan Umum (*Anti-Patterns*)

#### A. Mendokumentasikan Keputusan Melalui Architecture Decision Record (ADR)

Di proyek berdurasi 18 bulan dengan 18 personel vendor dan banyak pemangku kepentingan, keputusan arsitektur yang hanya disepakati secara lisan di ruang rapat akan terlupakan 6 bulan kemudian—memicu perdebatan ulang yang membuang waktu atau perubahan ceroboh oleh *developer* baru. **Architecture Decision Record (ADR)** (dipopulerkan Michael Nygard) adalah dokumen ringkas (1–2 halaman, disimpan di repositori Git layaknya kode sumber) yang mencatat:
1. **Judul & Status** (*Proposed, Accepted, Deprecated, Superseded by ADR-XXX*)
2. **Konteks & Pendorong Keputusan (*Context & Drivers*):** Fakta bisnis, NFR, anggaran, kendala tim, dan tenggat yang memaksa keputusan diambil.
3. **Opsi yang Dievaluasi (*Options Considered*):** Minimal 2–3 alternatif nyata beserta analisis pro–kontra objektif.
4. **Keputusan Terpilih (*Decision*):** Pilihan final dan alasan utamanya.
5. **Konsekuensi & Mitigasi (*Consequences & Trade-offs*):** Dampak positif, *trade-off* negatif yang diterima secara sadar, serta rencana mitigasi atau syarat peninjauan ulang di masa depan.

#### B. Lima Kesalahan Umum Arsitektur di Lapangan (*Anti-Patterns*)

| No | *Anti-Pattern* | Gejala di Lapangan | Dampak Fatal pada Proyek OMNI | Penangkal Arsitektural |
|----|----------------|--------------------|-------------------------------|------------------------|
| **1** | ***Distributed Monolith* / *Premature Microservices*** | Sistem dipecah jadi 20+ layanan mikro, tetapi semuanya masih harus di-*deploy* serentak dan saling panggil sinkron secara berantai | Kompleksitas operasional naik 5×, jadwal 14 Sprint jebol, vendor PT NDS mengajukan *Change Request* besar | Mulai dari **Modular Monolith** atau **Right-Sized Domain Services (5–6 layanan)** sesuai *Bounded Contexts* & kapasitas 18 personel |
| **2** | ***Shared Database Anti-Pattern*** | Layanan OMS, Loyalty, dan Adaptor POS membaca dan menulis langsung ke tabel basis data yang sama milik ERP lama | Perubahan satu kolom di ERP-Refresh merusak OMS dan Loyalty serentak; mustahil *scaling* mandiri | Terapkan **Database-per-Service** (isolasi skema/DB per domain) dan akses lintas domain hanya via **API atau Event** |
| **3** | ***Chatty Synchronous Chains*** | Alur *checkout* memanggil 7 layanan + ERP + Notifikasi secara sinkron berurutan | Ketersediaan majemuk anjlok: 7 layanan × 99,5% = $0{,}995^7 = \mathbf{96{,}55\%}$! Gagal total dari target ≥ 99,5% | Pisahkan jalur kritis (*checkout*) dari efek samping asinkron via **Event Bus + Outbox**, pasang **Circuit Breaker** |
| **4** | ***Ignoring RPO/RTO & False HA*** | Mengira punya 2 server di 1 pusat data sudah "DR", atau sebaliknya memesan *Active-Active* lintas negara tanpa analisis biaya | Gagal pulih saat bencana/ransomware, atau anggaran cloud menelan habis pos CB-03 Rp 1,15 M | Definisikan **RPO & RTO eksplisit** bersama bisnis, bedakan HA Multi-AZ dari DR *Warm Standby*, uji *DR Drill* berkala |
| **5** | ***Cloud Bill Shock*** | Memilih ukuran server terbesar 24/7 demi aman untuk uji beban 2.500 TPM dan membiarkan Dev/Staging menyala terus | Tagihan cloud membengkak 2–3× lipat di tengah proyek, memicu intervensi keras CFO Budi Santoso | Terapkan **FinOps** sejak Hari 1: *Auto-Scaling*, *Scale-to-Zero* non-prod, *tagging*, dan *budget alerts* |

---

## 6. Studi Kasus: Penerapan pada Proyek OMNI

Menjelang **Gate 1 (31 Juli 2026)**, **Dimas Prasetyo** (Lead Solution Architect) bersama **Irwan Pratama** (CTO) menyusun paket Cetak Biru Arsitektur Solusi Proyek OMNI untuk ditinjau bersama **Fajar Nugroho** (Senior PM), **Rina Kartika** (Head of Legal & InfoSec), **Siti Rahmawati** (Head of Supply Chain), **Agus Setiawan** (Head of Store Ops), serta **Bambang Hartono** (Delivery Director PT NDS). Berikut empat artefak arsitektur inti yang dihasilkan dan dikunci sebagai *Architecture Baseline*.

### 6.1 Cetak Biru Kontrak API Inti (5 Endpoint REST + Event Schema Kafka)

Dengan pendekatan *Contract-First* (OpenAPI 3.1), ditetapkan lima kontrak REST API paling kritis beserta satu skema *event* utama sinkronisasi stok.

#### Matriks 5 Endpoint REST Inti Proyek OMNI

| No | Endpoint & Metode | Konsumen → Layanan | Tujuan Bisnis | Pola Keamanan & Ketahanan | SLA Latensi (p95) |
|----|-------------------|--------------------|---------------|---------------------------|-------------------|
| **1** | `GET /v1/catalog/skus/{sku}/availability?lat={lat}&lng={lng}&radius_km=15` | Mobile/Web BFF → Catalog & Inventory | Menampilkan stok *near-real-time* di DC & daftar toko terdekat (*Click & Collect*) | API Key / JWT; *Cache-Aside* Redis (TTL 30 dtk) + Elasticsearch *geo-query*; *Rate limit* 120 req/mnt/IP | ≤ 150 ms |
| **2** | `POST /v1/inventory/reservations` | OMS Orchestrator → Inventory Service | Mengunci sementara (*hold* 15 mnt) stok toko/DC saat *checkout* agar bebas *overselling* | mTLS internal + wajib header **`Idempotency-Key`**; Redis atomic lock + PostgreSQL ACID commit | ≤ 200 ms |
| **3** | `POST /v1/orders` | Mobile/Web BFF → OMS Orchestrator | Membuat pesanan (Delivery / *Click & Collect*) & memulai **Saga Orchestration** (Stok + Poin + FinPay) | OAuth 2.0 JWT (`role: CUSTOMER`); wajib **`Idempotency-Key`**; *Transactional Outbox* | ≤ 450 ms |
| **4** | `PATCH /v1/stores/{store_code}/fulfillment/orders/{order_id}` | Store Fulfillment App (Tablet) → OMS | Staf toko memperbarui status BOPIS (`PICKING` → `READY_FOR_PICKUP` / `SHORT_PICK`) | JWT (`role: STORE_STAFF` + klaim `store_code` cocok — anti-BFLA/BOLA); *Optimistic Locking* (`version`) | ≤ 300 ms |
| **5** | `POST /v1/webhooks/payments/finpay` | PT FinPay Nusantara → Payment Adapter | Menerima callback status pembayaran (`SETTLED` / `FAILED` / `EXPIRED`) secara asinkron | Verifikasi *signature* `X-FinPay-Signature` (HMAC-SHA256) + *IP Allowlist* + *Idempotent Consumer* | ≤ 250 ms |

#### Contoh Spesifikasi Payload JSON (`POST /v1/orders`)

**Request Headers & Body:**
```http
POST /v1/orders HTTP/1.1
Host: api.sinarnusantara.co.id
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
Idempotency-Key: 9b2f7c10-4a8e-4f13-a7c2-7e9f1b4c8012
X-Correlation-ID: corr-omni-20271112-88421
Content-Type: application/json
```

```json
{
  "fulfillment_type": "CLICK_AND_COLLECT",
  "pickup_store_code": "JKT-014",
  "items": [ { "sku": "SKU-88210", "quantity": 2, "expected_unit_price_idr": 249000 } ],
  "loyalty_redemption": { "points_to_redeem": 500, "voucher_code": "OMNI-NOV27" },
  "payment_method": "QRIS_FINPAY"
}
```

**Response (`201 Created`):**
```json
{
  "order_id": "ORD-20271112-009412",
  "status": "AWAITING_PAYMENT",
  "reservation_id": "RSV-901442",
  "reservation_expires_at": "2027-11-12T10:25:00+07:00",
  "pricing_summary_idr": { "subtotal": 498000, "loyalty_discount": 50000, "grand_total": 448000 },
  "payment_session": {
    "provider": "FINPAY_NUSANTARA",
    "qris_payload_url": "https://pay.finpay.co.id/s/tok_8f91a2c",
    "expires_at": "2027-11-12T10:25:00+07:00"
  },
  "sla_pickup_estimate": "Siap diambil maksimal 2 jam setelah pembayaran terverifikasi"
}
```

#### Skema Event Kafka / Cloud PubSub (`inventory.updated` — Topic: `omni.inventory.events.v1`)

Untuk menjamin konsistensi stok **≤ 60 detik** di seluruh 120 toko dan 3 DC serta memberi umpan ke **Proyek DataHub**, setiap perubahan stok (penjualan kasir POS, penerimaan barang DC, reservasi online, atau pembatalan *Saga*) menerbitkan pesan berpartisi berdasarkan `partition_key = "{location_code}:{sku}"` (menjamin urutan kronologis per SKU per lokasi!):

```json
{
  "specversion": "1.0",
  "event_id": "evt-inv-7f3c91b2-991a-44c0-b012-109a3c442108",
  "event_type": "inventory.updated",
  "event_time": "2027-11-12T10:10:04.312+07:00",
  "source": "acl-pos-modern",
  "correlation_id": "corr-pos-jkt014-55201",
  "data": {
    "location_type": "STORE",
    "location_code": "JKT-014",
    "sku": "SKU-88210",
    "sequence_number": 48291,
    "delta_qty": -1,
    "on_hand_qty": 7,
    "reserved_qty": 2,
    "safety_stock_qty": 1,
    "available_to_promise_qty": 4,
    "reason_code": "POS_OFFLINE_SALE"
  }
}
```

> **Catatan Arsitektur Kritis:** Atribut `sequence_number` digunakan untuk mencegah *out-of-order overwrite* (jika *event* lama datang terlambat setelah jaringan toko pulih, konsumen mengabaikan pembaruan yang nomor urutnya lebih kecil), sedangkan `safety_stock_qty` (stok penyangga 1–2 unit per SKU laris di toko) melindungi risiko *overselling* di jeda waktu barang diambil pelanggan fisik dari rak sebelum dibayar di kasir!

---

### 6.2 Strategi Polyglot Persistence & Perhitungan Kapasitas Beban 2.500 TPM

Untuk membuktikan kepada CTO **Irwan Pratama** dan QA Lead **Lukas Gunawan** bahwa arsitektur lulus uji beban **2.500 TPM** (risiko **R-06**), Dimas menyusun model kalkulasi kapasitas kuantitatif berikut:

1. **Konversi Beban Transaksi Puncak (*Write Throughput*):**
   - Beban puncak berkelanjutan (*Sustained Peak*) = $\frac{2.500\text{ transaksi}}{60\text{ detik}} = \mathbf{41{,}67\text{ TPS}}$ (~**42 TPS**).
   - Faktor lonjakan seketika Harbolnas (*Peak Burst Factor* = **3×** pada 5 menit pembukaan promo) = $41{,}67 \times 3 = \mathbf{125\text{ TPS}}$ (*write/checkout* per detik).
2. **Proyeksi Beban Baca (*Read Throughput*) & Sinkronisasi:**
   - Dengan rasio Baca:Tulis omnichannel **20:1**, beban baca *sustained peak* = $41{,}67 \times 20 \approx \mathbf{833\text{ RPS}}$, dan beban baca *peak burst* = $125 \times 20 = \mathbf{2.500\text{ RPS}}$.
   - Arus *event* sinkronisasi stok POS (120 toko × ~1 transaksi kasir/10 detik saat ramai) + WMS 3 DC ≈ **150 event/detik** (puncak).
   - Total trafik API Gateway *peak burst* = $2.500 + 125 + 150 = \mathbf{2.775\text{ RPS}}$. Ditambah *safety headroom* **30%**, kapasitas desain target = **3.600 RPS**.
3. **Alokasi Penyimpanan & Anggaran Latensi Sinkronisasi (≤ 60 Detik):**
   - **Redis Cluster (3 shard × Primary+Replica, 16 GB RAM total):** Menyerap ≥ 85% trafik baca katalog & *stock lookup* (< 2 ms) serta 125 TPS *atomic lock* reservasi.
   - **Elasticsearch (3 node data lintas 3 AZ):** Menangani 18.500 dokumen SKU (~180 MB indeks—sangat ringan masuk penuh di memori *OS page cache*) + *geo-index* 120 toko dengan latensi kueri p95 < 40 ms.
   - **PostgreSQL Multi-AZ (Primary 8 vCPU / 32 GB RAM + 2 Read Replicas 4 vCPU / 16 GB RAM):** Menangani 125 TPS *write* ACID dengan nyaman (utilisasi CPU proyeksi < 45% pada *peak burst*, menggunakan PgBouncer *connection pooling* dan *monthly table partitioning*).
   - **MongoDB / DocumentDB (3-node Replica Set):** Menyimpan master dokumen kaya 18.500 SKU (~2,5 GB dengan riwayat revisi).
   - **Anggaran Latensi Sinkronisasi Stok (*End-to-End*):** POS lokal → Adaptor (2 dtk) + Jaringan ke Event Bus (3 dtk) + Inventory Service *commit* PG/Redis/ES (5 dtk) + Propagasi *cache invalidation* BFF (≤ 15 dtk) = **total p95 10–25 detik**, memberikan margin keamanan **35 detik** di bawah SLA maksimal **60 detik**.

---

### 6.3 Architecture Decision Record: ADR-001 (Granularitas Layanan Proyek OMNI)

| Field | Isi Keputusan Resmi |
|-------|---------------------|
| **ID & Judul** | **ADR-001: Pemilihan Arsitektur 6 *Right-Sized Domain Services* + *Event Bus* (Menolak *Full 25 Microservices* maupun *Single Monolith*)** |
| **Tanggal & Status** | 18 Juli 2026 — **ACCEPTED** (Disetujui oleh Irwan Pratama [CTO], Fajar Nugroho [Senior PM], dan Bambang Hartono [PT NDS]) |
| **Konteks & Pendorong** | 1) Tenggat mutlak 26 Nov 2027 (14 Sprint × 2 minggu); 2) Tim engineering PT NDS berjumlah 18 orang total (~11 developer aktif) + 3 *shared architect* SNR; 3) Target beban 2.500 TPM (125 TPS *burst*) dengan kebutuhan skalabilitas independen tinggi pada **Catalog/Search** dan **Inventory Sync**; 4) Pagu CB-02 Rp 1,65 M & CB-03 Rp 1,15 M. Proposal awal PT NDS mengusulkan pemecahan ke 25 *microservices* granular. |
| **Opsi 1: Single Monolith** | *Pro:* Cepat dimulai di Sprint 1–4, biaya operasional rendah. *Kontra:* Katalog (baca tinggi) dan OMS/Inventory (tulis ACID) tak bisa di-*scale* terpisah; risiko *blast radius* 100% jika integrasi POS bermasalah; bentrok *merge* 11 developer di satu basis kode. |
| **Opsi 2: Full 25 Microservices** *(Usulan Awal Vendor)* | *Pro:* Isolasi maksimal di atas kertas. *Kontra:* Rasio 2,3 layanan per developer → memicu *Distributed Monolith*, ledakan biaya CI/CD, *observability*, & transaksi terdistribusi lintas 25 DB; mengancam mundurnya Release 1–3 dan pembengkakan biaya Cloud di atas CB-03. |
| **Opsi 3: 6 Right-Sized Domain Services + 3 BFF + Event Bus** *(Terpilih)* | Memecah sistem tepat pada 6 *Bounded Contexts* DDD (Catalog/Search, Inventory, OMS/BOPIS, Loyalty, Payment/Shipping Adapter, Notification/Consent) ditambah ACL ERP/POS terpisah. Rasio ideal ~2 developer per domain; *scaling* independen pada titik panas (*hot path*); batas data jelas (*Database-per-Service* logis di klaster terkelola). |
| **Konsekuensi & Mitigasi** | **Positif:** Kecepatan *delivery* terjaga, toleransi kegagalan terisolasi, biaya cloud hemat ±40% dibanding 25 layanan. **Trade-off Negatif:** Tetap membutuhkan *Saga Orchestration*, *Outbox Pattern*, dan *OpenTelemetry Tracing* antar 6 layanan. **Mitigasi:** Standarisasi *shared template* Terraform, CI/CD, dan OpenAPI 3.1 sejak Sprint 0 (Agustus 2026). Peninjauan ulang pemecahan layanan lebih lanjut baru dilakukan pasca-2028 jika trafik > 10.000 TPM atau tim engineering > 40 orang. |

---

### 6.4 Rencana Cloud Multi-AZ Jakarta, DR (RPO/RTO), FinOps & Kepatuhan Regulasi

Berikut penyelarasan rancangan infrastruktur, keamanan, dan pagu anggaran **CB-02 (Rp 1,65 M)** serta **CB-03 (Rp 1,15 M)** yang disetujui CTO, CFO, dan Head of Legal/InfoSec:

1. **Rincian Realisasi FinOps Pagu CB-03 (Total = Rp 1.150 jt / Rp 1,15 M):**
   - **Pengadaan & Distribusi 240 Tablet/Scanner Toko** (2 unit × 120 toko @ Rp 2,25 jt termasuk *rugged case*, lisensi MDM, dan logistik ke luar Jawa): **Rp 540 jt** (47,0%).
   - **Keamanan & Kepatuhan Regulasi** (*Penetration Testing* independen 2 putaran oleh konsultan tersertifikasi CREST/OSCP, audit & pendampingan UU PDP, sertifikasi PCI-DSS SAQ-A, lisensi WAF/SIEM/KMS): **Rp 190 jt** (16,5%).
   - **Infrastruktur Cloud Region Jakarta (16 bulan selama masa proyek — Agu 2026 s.d. Nov 2027):** Dev/Staging *auto-stop* malam/akhir pekan (Rp 7 jt/bln × 16 = Rp 112 jt) + Lingkungan Load Test sementara (Rp 28 jt) + Produksi Multi-AZ bertahap selama Pilot & Wave Rollout 8 bulan + cadangan puncak Harbolnas 12.12 + DR *Warm Standby* (rata-rata Rp 35 jt/bln × 8 = Rp 280 jt) = **Rp 420 jt** (36,5%).
   - **Total CB-03 = Rp 540 jt + Rp 190 jt + Rp 420 jt = Rp 1.150 jt (Rp 1,15 M — 100% sesuai *Cost Baseline*!)**. *(Biaya operasional cloud tahun 2028 dan seterusnya masuk ke anggaran OPEX IT tahunan PT SNR, diproyeksikan ~Rp 38–45 jt/bulan pada beban penuh 500.000 MAU).*
2. **Rincian Pagu CB-02 Integrasi Legacy (Total = Rp 1.650 jt / Rp 1,65 M):**
   - API Gateway, BFF, & Managed Event Bus + DLQ/Observability: **Rp 420 jt**.
   - ACL & Adaptor Integrasi ERP-Refresh serta WMS 3 DC (Cikarang, Surabaya, Medan): **Rp 480 jt**.
   - ACL & Adaptor POS-Modern 120 Toko (termasuk *offline delta queue* & *mock sandbox*): **Rp 450 jt**.
   - Integrasi Payment Gateway PT FinPay Nusantara & Agregator Kurir: **Rp 300 jt**.
   - **Total CB-02 = Rp 1.650 jt (Rp 1,65 M)**.
3. **Target Ketersediaan & Pemulihan Bencana:**
   - **Desain Internal HA Multi-AZ Jakarta:** ≥ **99,9%** (maks. *downtime* 8,76 jam/tahun) — memberi *safety buffer* besar terhadap komitmen SLA bisnis **≥ 99,5%** (maks. *downtime* **43,8 jam/tahun**).
   - **Target DR (*Warm Standby* + *Immutable WAL Backup*):** **RPO ≤ 5 menit**, **RTO ≤ 30 menit**, wajib lulus simulasi *DR Failover Drill* sebelum Gate 3 (Juli 2027).
4. **Matriks Penandatanganan Kepatuhan Rina Kartika (Prasyarat Mutlak *Go-Live*):**
   - 100% data primer & cadangan tersimpan di **Region Jakarta** (UU PDP).
   - 0 penyimpanan data kartu PAN/CVV di server SNR (tertokenisasi via PT FinPay — PCI-DSS).
   - Fitur *Consent Management*, *Data Export*, dan *PII Anonymization* lulus UAT Legal.
   - Laporan *Penetration Testing* independen mencatatkan **0 temuan Critical dan 0 temuan High**; seluruh temuan *Medium* memiliki rencana remediasi bertanggal.

---
## 7. Latihan dan Pembahasan

### 7.1 Soal Latihan

Kerjakan empat studi kasus praktis berikut sebagai **Senior Solution Architect** pendamping **Dimas Prasetyo** pada Proyek OMNI PT Sinar Nusantara Retail.

#### Latihan 1: Desain Kontrak API & *Idempotency* Reservasi Stok *Click & Collect*
Saat simulasi beban *Click & Collect*, ditemukan insiden serius: pelanggan di jaringan seluler 4G yang tidak stabil menekan tombol *"Pesan & Ambil di Toko"* dua kali karena layar sempat membeku 3 detik. Akibatnya, sistem mengunci **2× jumlah stok** di Toko `SBY-004` (Surabaya) dan membuat dua nomor reservasi berbeda untuk satu pesanan yang sama.
**Tugas Anda:**
1. Rancang kontrak RESTful API yang tepat untuk *endpoint* reservasi stok (`Method`, `URI`, `Headers` wajib, contoh *Request JSON*, dan *Response JSON* untuk skenario sukses `201 Created`, pengulangan *idempotent* `200 OK`, serta stok tidak cukup `409 Conflict`).
2. Jelaskan mekanisme teknis di sisi *backend* (Redis + PostgreSQL) agar reservasi tersebut **100% idempoten**, **bebas *race condition*** saat 50 pelanggan berebut 1 stok terakhir, dan otomatis dilepas kembali jika pelanggan tidak membayar dalam 15 menit.

#### Latihan 2: Pola Integrasi & Parameter *Circuit Breaker* untuk 15 Toko Luar Jawa
**Agus Setiawan** (Head of Store Operations) melaporkan bahwa dari 120 toko SNR, terdapat **15 toko di luar Jawa** (Kalimantan, Sulawesi, dan sebagian Sumatra) yang mengalami gangguan koneksi internet berkala (*packet loss* tinggi atau putus 5–20 menit pada jam sibuk sore hari). Tim pengembang sempat mengusulkan agar aplikasi kasir POS di toko memanggil API OMS Jakarta secara **sinkron wajib** pada setiap transaksi kasir agar stok selalu *real-time*.
**Tugas Anda:**
1. Evaluasi usulan komunikasi sinkron wajib tersebut berdasarkan **Teorema CAP** dan risiko operasional 15 toko.
2. Rancang arsitektur integrasi pengganti yang aman bagi kasir toko sekaligus tetap mengejar target sinkronisasi stok **≤ 60 detik** saat koneksi normal (sebutkan pola *Outbox/Local Queue*, *Retry + Exponential Backoff & Jitter*, *Circuit Breaker*, *Idempotent Consumer*, dan *DLQ*).
3. Tetapkan konfigurasi konkret parameter **Circuit Breaker** (*sliding window*, ambang kegagalan, *timeout*, durasi *cooldown Open*, jumlah *probe Half-Open*, serta mekanisme *Fallback*).

#### Latihan 3: Kalkulasi Kapasitas, Anggaran *Downtime* 99,5%, & Biaya DR vs Pagu CB-03
Menjelang rapat Komite Arsitektur, seorang manajer bisnis mengusulkan menaikkan rancangan *cloud* dari **Multi-AZ Jakarta + DR Warm Standby** menjadi **Multi-Region Active-Active (Jakarta–Singapura)** dengan alasan *"ingin 99,99% uptime agar tidak pernah mati saat Harbolnas."* Sementara itu, CFO **Budi Santoso** mengingatkan bahwa total pagu pos **CB-03** adalah **Rp 1,15 M**, yang sudah harus menanggung **240 unit tablet/scanner toko (Rp 540 jt)** dan **PenTest + kepatuhan UU PDP/PCI-DSS (Rp 190 jt)**.
**Tugas Anda:**
1. Hitung konversi beban puncak **2.500 TPM** ke **TPS rata-rata** dan **peak burst 3×**, serta hitung anggaran *downtime* maksimal per tahun dan per bulan untuk **99,5%**, **99,9%**, dan **99,99% uptime**.
2. Hitung sisa pagu CB-03 yang tersedia untuk infrastruktur *cloud* selama 16 bulan masa proyek, lalu bandingkan kelayakan finansial opsi **Multi-AZ + Warm Standby** (estimasi Rp 26,25 jt/bln rata-rata 16 bln) melawan **Multi-Region Active-Active** (estimasi 2,8× biaya = Rp 73,5 jt/bln).
3. Berikan rekomendasi arsitektural sekaligus soroti implikasi **UU PDP** dari replikasi lintas negara ke Singapura.

#### Latihan 4: Menulis ADR Evaluasi Usulan Vendor PT NDS (18 Microservices)
Pada akhir Bulan ke-1, Delivery Director PT NDS (**Bambang Hartono**) mengajukan rancangan teknis yang memecah platform Proyek OMNI menjadi **18 microservices terpisah** (mis. `ProductService`, `CategoryService`, `PriceService`, `PromoService`, `StockService`, `ReservationService`, `CartService`, `OrderService`, `BopisService`, `MemberService`, `PointService`, `VoucherService`, dst.) dengan argumen *"agar arsitektur modern dan siap skala enterprise."* Padahal tim *developer* aktif PT NDS hanya 11 orang dan tenggat mutlak adalah 26 November 2027 (14 Sprint).
**Tugas Anda:**
Susun **Architecture Decision Record (ADR)** ringkas namun lengkap (*Konteks, Opsi yang Dievaluasi, Keputusan, Konsekuensi & Mitigasi*) yang akan Anda ajukan bersama Dimas Prasetyo kepada CTO **Irwan Pratama** untuk menolak usulan 18 *microservices* secara objektif, berdata, dan konstruktif.

---

### 7.2 Pembahasan Latihan

#### Pembahasan Latihan 1: Kontrak API & *Idempotency* Reservasi Stok *Click & Collect*

**1. Spesifikasi Kontrak API (`POST /v1/inventory/reservations`):**

- **Headers Wajib:**
  - `Authorization: Bearer <internal_mtls_or_service_jwt>`
  - `Idempotency-Key: <UUID-v4>` *(wajib dibuat oleh klien/OMS per satu niat transaksi; disimpan 24 jam)*
  - `X-Correlation-ID: <trace-correlation-id>`
  - `Content-Type: application/json`

- **Request Body:**
```json
{
  "order_reference": "ORD-20271112-004192",
  "location_type": "STORE",
  "location_code": "SBY-004",
  "ttl_seconds": 900,
  "items": [ { "sku": "SKU-44109", "quantity": 1 } ]
}
```

- **Response Skenario A — Sukses Baru (`201 Created`):**
```json
{
  "reservation_id": "RSV-20271112-77821",
  "idempotency_key": "5f8e1a20-92c1-4d3b-8e1a-772b09c12f44",
  "status": "RESERVED",
  "location_code": "SBY-004",
  "expires_at": "2027-11-12T14:30:00+07:00",
  "items": [ { "sku": "SKU-44109", "reserved_qty": 1, "remaining_atp_qty": 3 } ]
}
```

- **Response Skenario B — Permintaan Ulang dengan `Idempotency-Key` & Payload Sama (`200 OK`):**
  Server mengembalikan **objek reservasi yang persis sama** (`reservation_id: "RSV-20271112-77821"`) ditambah header `Idempotency-Replayed: true`, **tanpa** mengurangi stok kedua kalinya. *(Jika `Idempotency-Key` sama tetapi isi payload berbeda—mis. jumlah diganti dari 1 ke 2—server wajib menolak dengan `422 Unprocessable Entity` / `409 Conflict` untuk mencegah manipulasi).*

- **Response Skenario C — Stok Tidak Cukup (`409 Conflict`):**
```json
{
  "error_code": "INSUFFICIENT_STORE_INVENTORY",
  "message": "Stok tersedia di Toko SBY-004 tidak mencukupi untuk SKU-44109.",
  "details": {
    "sku": "SKU-44109",
    "requested_qty": 1,
    "available_to_promise_qty": 0,
    "suggested_nearest_stores": ["SBY-001", "SBY-007"]
  }
}
```

**2. Mekanisme Teknis Anti-*Race Condition* & Auto-Release:**
- **Lapisan Idempotency:** Gunakan tabel `idempotency_records(idempotency_key PRIMARY KEY, request_hash, response_status, response_body, created_at)` di PostgreSQL (dipercepat *lookup* Redis). Cek & simpan `idempotency_key` terjadi di dalam **satu transaksi ACID** bersama pemotongan stok sehingga tidak ada celah ganda saat dua permintaan datang di milidetik yang sama.
- **Lapisan Anti-*Race Condition* (50 Pelanggan Merebut 1 Stok):**
  - *Pintu Pertama (Redis Lua Script):* Jalankan skrip atomik Lua (`IF GET stock >= qty THEN DECRBY stock qty`) untuk menyaring 49 permintaan berlebih dalam < 2 ms tanpa membebani PostgreSQL.
  - *Pintu Kebenaran (PostgreSQL ACID):* Lakukan pembaruan bersyarat `UPDATE store_inventory SET reserved_qty = reserved_qty + 1, version = version + 1 WHERE store_code = 'SBY-004' AND sku = 'SKU-44109' AND (on_hand_qty - reserved_qty - safety_stock_qty) >= 1;`. Jika `rows_affected == 0`, kembalikan `409 Conflict` dan kembalikan counter Redis.
- **Auto-Release TTL 15 Menit:** Simpan kolom `expires_at = NOW() + INTERVAL '15 minutes'`. Jalankan *background sweeper* / *delayed message* setiap 30 detik yang mencari reservasi berstatus `RESERVED` dengan `expires_at < NOW()`, lalu dalam transaksi ACID mengubah status menjadi `EXPIRED`, mengurangi `reserved_qty`, menyinkronkan Redis, dan menerbitkan *event* `inventory.updated` ke Kafka.

---

#### Pembahasan Latihan 2: Integrasi & *Circuit Breaker* untuk 15 Toko Luar Jawa

**1. Evaluasi Usulan Sinkron Wajib (Perspektif CAP Theorem):**
Usulan mewajibkan kasir POS memanggil OMS Jakarta secara sinkron adalah **sangat berbahaya dan melanggar realitas CAP Theorem**. Saat terjadi partisi jaringan (**P**) di 15 toko luar Jawa selama 15 menit, arsitektur sinkron memaksa toko memilih *Consistency* (**CP**) dengan mengorbankan *Availability* (**A**) → akibatnya kasir fisik tidak bisa mencetak struk, antrean pelanggan mengular di toko, dan **Agus Setiawan** akan menolak penuh proyek OMNI (memicu risiko **R-03**). Untuk transaksi kasir fisik di toko, ketersediaan lokal (**AP**) bersifat mutlak!

**2. Arsitektur Integrasi Pengganti (Offline-Resilient Event-Driven):**
- **Local Store Outbox Queue (di POS Adaptor Toko):** Setiap transaksi kasir langsung tersimpan secara lokal (ACID) di basis data POS toko dalam < 200 ms dan langsung mencetak struk. Bersamaan dengan itu, baris delta stok ditulis ke tabel **Local Outbox** dengan `sequence_number` monotonik.
- **Pengiriman Asinkron + Batching Adaptif:** Agen sinkronisasi (*Store Sync Agent*) di toko memantau *Local Outbox* dan mengirim *event* delta stok ke API Gateway / Event Bus Jakarta tiap 2–5 detik (sehingga saat koneksi sehat, sinkronisasi *end-to-end* tercapai dalam **10–25 detik**, jauh di bawah SLA ≤ 60 detik).
- **Retry with Exponential Backoff & Jitter:** Saat koneksi internet toko putus, agen menerapkan jeda eksponensial (2 dtk → 4 dtk → 8 dtk → 16 dtk → maks. 60 dtk + *jitter* ±25%) agar ketika internet 15 toko pulih serentak tidak membanjiri API Gateway Jakarta.
- **Idempotent Consumer & Sequence Check:** Inventory Service di Jakarta mengecek `event_id` (anti-duplikat) dan `sequence_number` (anti-*out-of-order*). Pesan yang korup setelah 5× kegagalan logis dialihkan ke **DLQ** dengan *alert* ke tim IT Ops.
- **Proteksi *Overselling* Saat Toko Offline:** Apabila *heartbeat* toko `KLM-003` berhenti > 3 menit, OMS secara otomatis menandai toko tersebut berstatus `SYNC_DEGRADED` dan **menonaktifkan sementara opsi *Click & Collect* untuk stok tipis (≤ 3 unit)** di toko tersebut atau menaikkan *safety stock* sementara hingga koneksi pulih dan *backlog* antrean tuntas tersinkronisasi!

**3. Konfigurasi Parameter Circuit Breaker (OMS/ACL ↔ API Toko & ERP):**
- **Request Timeout:** `2.500 ms` (2,5 detik) per panggilan HTTP.
- **Sliding Window:** 20 permintaan terakhir (atau jendela waktu 30 detik, minimum 10 permintaan agar tidak sensitif terhadap 1 galat acak).
- **Failure Rate Threshold (`Closed → Open`):** ≥ **50%** permintaan gagal (`5xx` atau *timeout*) atau ≥ 5 *timeout* berturut-turut.
- **Open State Cooldown (`Open → Half-Open`):** **30 detik** (mencegah pemborosan *thread* ke toko/ERP yang sedang mati).
- **Half-Open Probe (`Half-Open → Closed/Open`):** Loloskan **3 permintaan uji coba**. Jika 3/3 sukses → kembali **Closed**; jika ≥ 1 gagal → kembali **Open** selama 30 detik (dengan peningkatan bertahap hingga maks. 120 detik).
- **Mekanisme Fallback saat Open:** Untuk transaksi dari toko ke pusat → tahan pesan di *Local Outbox* toko; untuk pembacaan stok pelanggan dari pusat → layani dari *snapshot* terakhir di Redis dengan flag `stock_freshness: "DELAYED"` dan terapkan proteksi batas *safety stock* otomatis.

---

#### Pembahasan Latihan 3: Kapasitas, Anggaran *Downtime* 99,5%, & Kelayakan FinOps CB-03

**1. Perhitungan Throughput & Anggaran *Downtime* (1 tahun = 8.760 jam = 525.600 menit):**
- **Sustained Peak Throughput:** $\frac{2.500\text{ TPM}}{60} = \mathbf{41{,}67\text{ TPS}}$ (~42 TPS *write*).
- **Peak Burst 3×:** $41{,}67 \times 3 = \mathbf{125\text{ TPS}}$ (*write*) dan dengan rasio Baca:Tulis 20:1 = **2.500 RPS** (*read*).
- **Anggaran *Downtime* Maksimal per Tingkat Ketersediaan:**

| Target Uptime | Rumus Downtime Tahunan | Maks. Downtime / Tahun | Maks. Downtime / Bulan (÷12) | Catatan Arsitektur |
|---------------|------------------------|------------------------|------------------------------|--------------------|
| **99,5%** *(SLA Bisnis OMNI)* | $0{,}5\% \times 8.760\text{ jam}$ | **43,8 jam** | **3,65 jam** (219 mnt) | Target kontrak bisnis Proyek OMNI |
| **99,9%** *(Desain Internal HA Multi-AZ)* | $0{,}1\% \times 8.760\text{ jam}$ | **8,76 jam** | **43,8 menit** | Memberi *safety margin* 5× lebih aman |
| **99,99%** *(Usulan Active-Active)* | $0{,}01\% \times 8.760\text{ jam}$ | **52,56 menit** | **4,38 menit** | Membutuhkan arsitektur *multi-region* kompleks |

**2. Analisis Kelayakan Finansial terhadap Pagu CB-03 (Rp 1,15 M = Rp 1.150 jt):**
- Komitmen wajib non-cloud dalam CB-03: 240 Tablet/Scanner (**Rp 540 jt**) + Keamanan, PenTest & Audit UU PDP (**Rp 190 jt**) = **Rp 730 jt**.
- **Sisa pagu CB-03 untuk Infrastruktur Cloud (16 bulan proyek):** $\text{Rp } 1.150\text{ jt} - \text{Rp } 730\text{ jt} = \mathbf{\text{Rp } 420\text{ jt}}$.
- **Opsi A (Multi-AZ Jakarta + DR Warm Standby):** $\text{Rp } 26{,}25\text{ jt/bln} \times 16\text{ bln} = \mathbf{\text{Rp } 420\text{ jt}}$ → **100% sesuai pagu CB-03 (defisit Rp 0)**.
- **Opsi B (Multi-Region Active-Active Jakarta–Singapura):** $\text{Rp } 73{,}5\text{ jt/bln} \times 16\text{ bln} = \mathbf{\text{Rp } 1.176\text{ jt}}$ (**Rp 1,18 M**) → **Defisit +Rp 756 jt** di atas anggaran cloud (bahkan melampaui seluruh pagu CB-03 Rp 1,15 M sebelum membeli satu pun tablet toko atau PenTest!). Ini akan menguras habis *Contingency Reserve* CB-06 (Rp 0,70 M) dan ditolak keras CFO Budi Santoso.

**3. Rekomendasi & Implikasi UU PDP:**
- **Tolak usulan Multi-Region Active-Active lintas negara.** Rekomendasikan **Multi-AZ Region Jakarta (3 AZ) + DR Warm Standby (RPO ≤ 5 menit, RTO ≤ 30 menit)** dengan target desain internal **99,9% uptime** (sudah 5× lebih ketat dari SLA 99,5%).
- **Implikasi UU PDP No. 27/2022 (Pasal 56):** Replikasi *Active-Active* data pribadi pelanggan (1,2 juta anggota) ke Singapura termasuk **transfer data pribadi ke luar wilayah hukum Indonesia**, yang mewajibkan verifikasi kesetaraan tingkat pelindungan negara tujuan, klausul kontrak tambahan, persetujuan eksplisit tambahan, dan berisiko memicu **veto dari Rina Kartika** menjelang tenggat 26 November 2027.

---

#### Pembahasan Latihan 4: ADR Evaluasi Usulan 18 Microservices PT NDS

- **ID & Judul:** `ADR-002: Penolakan Dekomposisi 18 Microservices PT NDS dan Penetapan 6 Modular Domain Services`
- **Status:** Proposed → Direkomendasikan **ACCEPTED** ke CTO Irwan Pratama.
- **Konteks & Data Fakta:** Vendor PT NDS mengusulkan 18 *microservices* (memecah hingga tingkat tabel seperti `CategoryService` terpisah dari `ProductService`, serta `PointService` terpisah dari `MemberService` dan `VoucherService`). Tim pengembang PT NDS berjumlah 11 developer aktif dengan kontrak *Fixed Price* Rp 4,40 M dan tenggat 14 Sprint (26 Nov 2027).
- **Analisis Opsi:**
  1. *Opsi 1 — 18 Microservices (Usulan NDS):* Rasio **1,64 layanan per developer**. Memecah entitas yang selalu berubah bersamaan (`Product + Category + Price` dan `Member + Point + Voucher`) melanggar prinsip kohesi DDD (*High Cohesion, Low Coupling*), memaksa panggilan jaringan berantai (*chatty RPC*), menurunkan ketersediaan majemuk, membutuhkan 18 *pipeline* CI/CD & basis data terpisah, serta memperbesar peluang vendor mengajukan *Change Request* biaya integrasi saat Sprint 7–11.
  2. *Opsi 2 — 6 Modular Domain Services (Rekomendasi SA):* Menggabungkan entitas berkohesi tinggi ke dalam satu *Bounded Context* (mis. `Catalog Service` mencakup Product+Category+Price; `Loyalty Service` mencakup Member+Point+Voucher). Rasio ideal **~1,8 developer per layanan**, tetap memenuhi skalabilitas independen untuk titik panas (Catalog & Inventory) dan meminimalkan transaksi terdistribusi.
- **Keputusan:** Menetapkan **6 Modular Domain Services + 3 BFF + 2 ACL** sesuai *Bounded Contexts* DDD; menolak dekomposisi 18 *microservices*.
- **Konsekuensi & Mitigasi:** Struktur kode di dalam masing-masing layanan tetap disusun modular secara paket (*clean modular boundaries*) sehingga apabila pasca-2028 salah satu sub-domain (mis. `Promo/Flash-Sale Engine`) tumbuh sangat masif, modul tersebut dapat diekstrak keluar dengan biaya migrasi minimal (*Evolutionary Architecture*).

---

## 8. Tugas Modul dan Rubrik Penilaian

### 8.1 Brief Tugas Mandiri (±6 Jam)

Anda bertindak sebagai **Lead Solution Architect** pendamping **Dimas Prasetyo** yang ditugaskan oleh CTO **Irwan Pratama** dan Senior PM **Fajar Nugroho** untuk menyusun paket **Solution Architecture Readiness Pack** bagi **Gate 1 Proyek OMNI** (siap dipresentasikan di hadapan *Steering Committee* & **Rina Kartika**). Susun dokumen terpadu berformat profesional yang memuat **empat komponen wajib** berikut:

1. **Solution Architecture Document (SAD) Ringkas Proyek OMNI (2–3 halaman):**
   - Diagram arsitektur *end-to-end* (boleh menggunakan Mermaid atau diagram vektor) mencakup lapisan klien, Edge/WAF, API Gateway/BFF, layanan domain, *Polyglot Persistence*, Event Bus + DLQ, ACL ERP/POS, PT FinPay Nusantara, dan Proyek DataHub.
   - Tabel pemetaan *Non-Functional Requirements* (NFR) Proyek OMNI (2.500 TPM, sinkronisasi ≤ 60 detik, ≥ 99,5% uptime, SLA BOPIS ≤ 2 jam, UU PDP & PCI-DSS) terhadap keputusan mekanisme arsitektur yang menjawabnya.
2. **Dua Dokumen Architecture Decision Record (ADR) Lengkap:**
   - **ADR-A:** Keputusan pemilihan **Database & Caching Strategy** (*Polyglot Persistence* vs *Single PostgreSQL*) untuk katalog 18.500 SKU dan reservasi stok anti-*overselling*.
   - **ADR-B:** Keputusan pemilihan **Pola Transaksi Terdistribusi & Integrasi Legacy** (*Saga Orchestration + Outbox + ACL* vs *Synchronous RPC / 2PC*) untuk alur *Click & Collect* dan mitigasi risiko keterlambatan **POS-Modern (R-01)**.
3. **Spesifikasi Kontrak API & Event (Contract-First):**
   - Rancang minimal **3 kontrak REST API** (berbeda dari contoh lengkap di Bagian 6.1, misalnya: pencarian stok toko terdekat, pembaruan status *Click & Collect* oleh staf toko `PATCH`, dan validasi/penebusan QR voucher loyalty di kasir POS) lengkap dengan metode HTTP, header keamanan/idempotency, *request/response JSON*, dan kode galat.
   - Rancang **1 Event Schema JSON** untuk topik `order.bopis.ready_for_pickup` atau `loyalty.points.redeemed` lengkap dengan `partition_key` dan strategi *idempotent consumer*.
4. **Rencana Cloud Multi-AZ, Disaster Recovery (RPO/RTO), FinOps & Kepatuhan UU PDP/PCI-DSS:**
   - Perhitungan kapasitas *peak burst* & anggaran *downtime* 99,5% vs target internal 99,9%.
   - Rencana DR (*RPO ≤ 5 menit, RTO ≤ 30 menit*) beserta jadwal *DR Drill* dan rincian alokasi biaya **CB-03 Rp 1,15 M** (tidak melampaui pagu, tetap mencadangkan 240 tablet/scanner & PenTest).
   - Daftar kendali teknis keamanan *Defense-in-Depth* (TLS 1.3, AES-256/KMS, tokenisasi FinPay, OWASP API Top 10, hak subjek data UU PDP, dan 3 pilar *Observability*) untuk memperoleh persetujuan **Rina Kartika**.

### 8.2 Rubrik Penilaian (Total Bobot = 100%)

| Kriteria Penilaian | Bobot | Skor 4: Sangat Baik (90–100) | Skor 3: Baik (75–89) | Skor 2: Cukup (60–74) | Skor 1: Perlu Perbaikan (< 60) |
|--------------------|------:|------------------------------|----------------------|-----------------------|--------------------------------|
| **1. Kelengkapan & Koherensi Cetak Biru SAD & Pemetaan NFR** | **25%** | Topologi *end-to-end* sangat jelas, konsisten 100% dengan ekosistem SNR (120 toko, 3 DC, ERP-Refresh, POS-Modern, DataHub, FinPay); setiap NFR terhubung langsung ke mekanisme arsitektur yang tepat tanpa *anti-pattern* | Topologi lengkap dan akurat; sebagian besar NFR dipetakan dengan baik meski ada beberapa detail interaksi antar-komponen atau *fallback* yang kurang tajam | Diagram terlalu konseptual/umum; masih terdapat celah ketergantungan sinkron berisiko *cascading failure* atau mengabaikan sistem paralel | Arsitektur tidak konsisten dengan studi kasus, mengandung *anti-pattern* fatal (*shared DB* / *direct legacy coupling*), atau tidak menjawab NFR |
| **2. Ketajaman Analisis *Trade-Off* pada 2 ADR** | **25%** | Kedua ADR memuat konteks kuantitatif tajam, membandingkan ≥ 3 opsi realistis secara adil, menyajikan *trade-off* negatif secara jujur, serta dilengkapi rencana mitigasi & syarat peninjauan ulang | Kedua ADR terstruktur baik dengan opsi pembanding logis dan keputusan tepat; analisis *trade-off* negatif atau mitigasi sedikit kurang mendalam | ADR cenderung hanya membenarkan satu teknologi favorit (*confirmation bias*) tanpa membandingkan opsi alternatif secara kuantitatif | Tidak mengikuti format ADR, tidak menyajikan opsi alternatif maupun *trade-off*, atau keputusan bertentangan dengan kendala tim/anggaran |
| **3. Kualitas Teknis Kontrak REST API & Event Schema** | **25%** | Seluruh 3 endpoint REST mematuhi standar penamaan, metode HTTP, status code presisi, `Idempotency-Key`, RBAC anti-BOLA/BFLA, dan payload JSON valid; *Event Schema* mencantumkan `event_id`, `partition_key`, dan strategi *Outbox/DLQ* | Kontrak REST dan *Event Schema* sebagian besar valid dan rapi; terdapat kekurangan minor pada penanganan kode galat (`409/429`) atau kunci partisi | Desain API belum sepenuhnya RESTful (mis. memakai kata kerja di URI), lupa *idempotency* pada aksi tulis, atau *Event Schema* tidak membahas duplikasi pesan | Payload JSON tidak valid, melanggar prinsip keamanan dasar (mis. mengirim data kartu/PII mentah tanpa proteksi), atau tidak menyertakan skema *event* |
| **4. Akurasi Cloud Multi-AZ, RPO/RTO, FinOps CB-03 & Kepatuhan UU PDP/PCI-DSS** | **25%** | Seluruh hitungan kapasitas (2.500 TPM / 125 TPS), anggaran *downtime* (43,8 jam/thn), RPO/RTO, dan alokasi **CB-03 Rp 1,15 M** 100% tepat; kendali UU PDP (residensi, *consent*, anonimisasi), PCI-DSS tokenisasi, OWASP & *Observability* siap audit Rina Kartika | Perhitungan kapasitas, DR, dan pagu CB-03 akurat; kendali keamanan & *Observability* memadai meski beberapa rincian UU PDP (mis. anonimisasi tanpa merusak pembukuan) kurang spesifik | Terdapat kekeliruan kecil pada hitungan biaya/kapasitas, mencampuradukkan HA dan DR, atau daftar keamanan bersifat normatif tanpa mekanisme teknis konkret | Melampaui pagu CB-03 / melupakan biaya 240 tablet & PenTest, melanggar residensi UU PDP / PCI-DSS, atau mengabaikan RPO/RTO dan *Observability* |

---

## 9. Kuis dan Kunci Jawaban

### 9.1 Soal Kuis

Pilihlah **satu jawaban yang paling tepat** (A, B, C, atau D) untuk setiap skenario level senior berikut.

**1.** Pada fitur *checkout* Aplikasi Mobile Proyek OMNI, seorang pelanggan menekan tombol *"Konfirmasi Pesanan"* di area parkir mal dengan sinyal lemah sehingga permintaan `POST /v1/orders` mengalami *timeout* di layar dan aplikasi otomatis melakukan *retry* 2 detik kemudian. Mekanisme desain API manakah yang paling tepat untuk mencegah terciptanya dua pesanan ganda dan pemotongan poin loyalty dua kali?
- A. Mengubah metode HTTP pembuatan pesanan dari `POST` menjadi `GET` agar secara alami bersifat *idempotent*.
- B. Mematikan seluruh fitur *retry* di aplikasi mobile dan meminta pelanggan memeriksa mutasi rekening sendiri.
- C. Mewajibkan klien mengirimkan header **`Idempotency-Key`** (UUID v4 unik per niat transaksi) yang divalidasi dan disimpan secara atomik bersama transaksi pesanan di server sehingga *retry* mengembalikan hasil transaksi pertama.
- D. Memasang jeda paksa (*sleep*) 10 detik di API Gateway untuk setiap permintaan `POST /v1/orders`.

**2.** Dimas Prasetyo sedang memilih protokol komunikasi untuk tiga kebutuhan berbeda pada Proyek OMNI: (i) menerima notifikasi asinkron status pembayaran dari **PT FinPay Nusantara**, (ii) komunikasi internal berlatensi sangat rendah antara *OMS Orchestrator* dan *Inventory Service*, serta (iii) API publik untuk aplikasi Mobile/Web dan adaptor mitra kurir. Kombinasi protokol manakah yang paling tepat?
- A. (i) gRPC, (ii) Webhook, (iii) GraphQL.
- B. (i) **Webhook** (dengan verifikasi HMAC-SHA256), (ii) **gRPC** (HTTP/2 + Protobuf), dan (iii) **REST** (HTTP/JSON + OpenAPI).
- C. (i) REST Polling setiap 1 detik, (ii) Webhook, (iii) gRPC langsung dari browser Web.
- D. Menggunakan SOAP/XML untuk ketiganya agar seragam dengan ERP lama tahun 2012.

**3.** Dalam merancang strategi *Polyglot Persistence* Proyek OMNI (18.500 SKU dengan atribut beragam di 8 kategori, pencarian teks + toko terdekat dari 120 toko, *distributed stock lock*, serta transaksi pesanan dan mutasi poin loyalty), pasangan domain dan teknologi basis data manakah yang paling tepat?
- A. Menyimpan seluruh pesanan, ledger poin, pencarian teks, dan *cache* sesi dalam satu *instance* MongoDB agar tidak perlu mempelajari banyak teknologi.
- B. Menggunakan Elasticsearch sebagai satu-satunya *system of record* untuk saldo poin loyalty dan transaksi pembayaran karena pencariannya paling cepat.
- C. Menyimpan seluruh katalog 18.500 SKU dan transaksi pesanan hanya di Redis tanpa persistensi disk agar latensi selalu di bawah 2 ms.
- D. Menggunakan **PostgreSQL (ACID)** untuk Order, Reservasi Stok & Ledger Poin; **MongoDB** untuk atribut katalog fleksibel; **Redis** untuk *caching* & *atomic stock lock*; serta **Elasticsearch** untuk pencarian teks bebas & *geo-distance* 120 toko.

**4.** Selama persiapan Harbolnas 12.12, beberapa toko SNR di Kalimantan mengalami putus koneksi internet ke Jakarta selama 15 menit. Menurut **Teorema CAP** dan realitas operasional ritel, keputusan arsitektur manakah yang paling tepat untuk menyeimbangkan integritas stok online dan kelancaran operasional kasir fisik di toko?
- A. Menerapkan **AP (*Availability + Eventual Consistency*)** pada kasir fisik POS toko melalui *Local Outbox Queue* agar toko tetap bisa melayani pembeli fisik saat offline, sekaligus menerapkan **CP (*Strong Consistency*)** pada *checkout* online dan menonaktifkan sementara *Click & Collect* stok tipis di toko yang berstatus *offline*.
- B. Menerapkan **CP** mutlak pada mesin kasir POS toko sehingga kasir otomatis terkunci dan tidak dapat melayani pembeli fisik selama internet ke Jakarta putus.
- C. Menerapkan **CA** (*Consistency + Availability*) penuh pada seluruh 120 toko dengan mengabaikan *Partition Tolerance* karena jaringan internet modern tidak mungkin putus.
- D. Menghentikan seluruh sinkronisasi *near-real-time* dan kembali ke sinkronisasi *batch* pukul 00.00 WIB seperti sistem lama.

**5.** Vendor PT NDS memiliki 11 *developer* aktif dan mengusulkan memecah platform Proyek OMNI menjadi 24 *microservices* granular sejak Sprint 1. Berdasarkan prinsip *Domain-Driven Design* (*Bounded Contexts*), *Conway's Law*, dan kendala tenggat 26 November 2027, risiko utama apa yang paling mungkin terjadi jika usulan tersebut disetujui mentah-mentah?
- A. Kinerja aplikasi otomatis naik 24 kali lipat dan biaya *cloud* CB-03 turun drastis karena ukuran tiap layanan menjadi sangat kecil.
- B. Terjebak dalam ***Distributed Monolith* (*Premature Microservices*)**: rasio > 2 layanan per *developer* memicu *overhead* CI/CD, kompleksitas transaksi terdistribusi, latensi jaringan berantai, pembengkakan biaya *cloud*, dan keterlambatan jadwal.
- C. Tim QA tidak perlu lagi melakukan *System Integration Testing* (SIT) karena tiap layanan sudah memiliki basis data masing-masing.
- D. Ketergantungan terhadap proyek paralel POS-Modern dan ERP-Refresh otomatis hilang tanpa perlu *Anti-Corruption Layer*.

**6.** Pada alur *Event-Driven Architecture*, OMS menyimpan pesanan baru ke PostgreSQL lalu pada baris kode berikutnya menerbitkan *event* `order.created` ke Apache Kafka. Suatu malam, kontainer OMS mendadak *crash* tepat setelah `COMMIT` PostgreSQL berhasil, namun sebelum *event* terkirim ke Kafka (*Dual-Write Problem*)—akibatnya pesanan tidak pernah masuk ke antrean gudang DC Cikarang. Pola integrasi manakah yang menyelesaikan masalah ini secara tuntas?
- A. Pola *Backend for Frontend* (BFF) dengan menambahkan kompresi Gzip pada respons HTTP.
- B. Pola *Cache-Aside* dengan memperpanjang TTL Redis menjadi 7 hari.
- C. Pola ***Transactional Outbox*** (menyimpan baris pesanan dan baris *event* ke tabel `outbox_events` dalam **satu transaksi ACID PostgreSQL yang sama**, lalu proses *CDC/Relay* mengirimkannya ke Kafka) dipadukan dengan ***Idempotent Consumer***.
- D. Menghapus Kafka dan menggantinya dengan panggilan sinkron langsung dari OMS ke server WMS DC Cikarang, DC Surabaya, dan DC Medan.

**7.** Pada alur pesanan *Click & Collect* (BOPIS) Proyek OMNI, pelanggan telah berhasil membayar Rp 448.000 melalui QRIS PT FinPay Nusantara dan menukarkan 500 poin loyalty. Satu jam kemudian, staf Toko `BDG-002` melaporkan melalui *Store Fulfillment App* bahwa barang terakhir di rak ternyata retak (*short-pick*). Dalam pola **Saga Orchestration**, langkah apakah yang harus dieksekusi oleh *OMS Orchestrator*?
- A. Menjalankan perintah SQL `ROLLBACK` serentak lintas basis data OMS, Loyalty, dan server eksternal PT FinPay Nusantara melalui *Two-Phase Commit* (2PC).
- B. Membiarkan pesanan berstatus menggantung dan menunggu pelanggan menelepon *call center* untuk mengurus pengembalian dana secara manual minggu depan.
- C. Menghapus baris pesanan secara permanen (`DELETE FROM orders`) dari basis data agar laporan pembatalan tidak tercatat.
- D. Mengeksekusi rangkaian ***Compensating Transactions*** secara terorkestrasi: memicu *auto-refund* ke PT FinPay, mengembalikan 500 poin ke *Digital Loyalty Ledger*, mengoreksi stok toko = 0 disertai flag audit opname, memperbarui status pesanan, dan mengirim notifikasi ke pelanggan.

**8.** Koneksi API dari proyek paralel ERP lama sempat mengalami lonjakan latensi hingga 18 detik akibat proses tutup buku bulanan, sehingga seluruh *thread pool* OMS habis menunggu dan menyebabkan aplikasi mobile ikut lumpuh (*cascading failure*). Pola ketahanan dan mekanisme transisi status apakah yang paling tepat diterapkan untuk melindungi OMS?
- A. ***Circuit Breaker*** (`Closed` → **`Open`** ketika ambang kegagalan/timeout terlampaui agar langsung *fail-fast* ke *Fallback* → **`Half-Open`** setelah *cooldown* untuk menguji beberapa *probe* sebelum kembali ke `Closed`) dikombinasikan dengan *Retry + Exponential Backoff & Jitter*.
- B. Memperpanjang *HTTP timeout* dari 3 detik menjadi 300 detik dan menambahkan *infinite retry loop* tanpa jeda sampai ERP merespons.
- C. Mematikan enkripsi TLS 1.3 antar-layanan agar koneksi ke ERP menjadi lebih ringan.
- D. Menjalankan ulang (*restart*) seluruh 120 mesin kasir POS secara serentak setiap kali ERP melambat.

**9.** Target SLA bisnis Proyek OMNI menetapkan ketersediaan sistem **≥ 99,5% uptime** per tahun dan beban uji **2.500 TPM**, sementara sisa ruang pagu **CB-03** untuk infrastruktur *cloud* 16 bulan adalah **Rp 420 jt** (setelah 240 tablet/scanner & biaya keamanan/PenTest). Berapakah batas maksimum *downtime* tahunan pada 99,5% uptime, dan strategi HA/DR manakah yang paling tepat untuk Proyek OMNI?
- A. Maks. *downtime* 52,56 menit/tahun; wajib memilih *Multi-Region Active-Active* Jakarta–Singapura agar aman tanpa perlu memperhatikan pagu CB-03 maupun UU PDP.
- B. Maks. *downtime* **43,8 jam/tahun** (~3,65 jam/bulan); strategi paling optimal adalah **High Availability Multi-AZ di Region Jakarta** (desain internal ≥ 99,9%) + **DR *Warm Standby*** (RPO ≤ 5 menit, RTO ≤ 30 menit) + disiplin **FinOps** (*auto-scaling* & *auto-stop* non-prod).
- C. Maks. *downtime* 438 jam/tahun; cukup menggunakan 1 server *Single-AZ* tanpa *backup* otomatis agar biaya *cloud* serendah mungkin.
- D. Maks. *downtime* 4,38 jam/tahun; cukup menggunakan *Backup & Restore* mingguan (RPO 7 hari, RTO 48 jam) karena pelanggan ritel tidak keberatan menunggu 2 hari.

**10.** Dalam tinjauan keamanan menjelang *Penetration Testing*, **Rina Kartika** (Head of Legal & InfoSec) mengajukan tiga tuntutan wajib: (1) lingkup audit **PCI-DSS** harus seminimal mungkin, (2) pelanggan dapat meminta penghapusan data pribadi sesuai **UU PDP** tanpa merusak integritas laporan pembukuan pajak pesanan 5 tahun terakhir, dan (3) mencegah pengguna biasa memanggil *endpoint* staf toko `PATCH /v1/stores/{store_code}/fulfillment/orders/{order_id}`. Rangkaian kendali arsitektur manakah yang menjawab ketiga tuntutan tersebut secara tepat?
- A. Menyimpan nomor kartu kredit terenkripsi Base64 di PostgreSQL; menghapus seluruh baris tabel `orders` saat pelanggan meminta hapus data; menyembunyikan URL *endpoint* staf toko tanpa otorisasi server.
- B. Mengirim data kartu melalui email terenkripsi ke PT FinPay; menolak semua permintaan penghapusan data UU PDP; membedakan staf dan pelanggan hanya lewat parameter query `?is_staff=true`.
- C. Menerapkan **Tokenisasi / Hosted Fields via PT FinPay Nusantara** (0 penyimpanan PAN/CVV di server SNR); memisahkan tabel PII dari fakta pesanan via `customer_uuid` sehingga hak hapus dilakukan lewat **anonimisasi/crypto-shredding PII** tanpa menghapus pembukuan; serta menegakkan **RBAC berbasis klaim JWT (`role: STORE_STAFF` + pencocokan `store_code`)** untuk menutup celah **OWASP API5 (BFLA) & API1 (BOLA)**.
- D. Memindahkan seluruh basis data ke server di luar negeri agar terbebas dari audit UU PDP dan menonaktifkan pencatatan *Structured Logs*.

---

### 9.2 Kunci Jawaban dan Pembahasan

| No | Kunci | Pembahasan Lengkap |
|----|-------|--------------------|
| **1** | **C** | **Benar:** Metode `POST` secara alami tidak idempoten. Mengirimkan header **`Idempotency-Key`** (UUID v4 unik per niat transaksi) dan menyimpannya secara atomik bersama pembuatan pesanan memastikan permintaan ulang (*retry*) mengembalikan respons pesanan pertama tanpa menggandakan pesanan maupun pemotongan poin.<br/>*Mengapa opsi lain salah:* Opsi A melanggar semantik HTTP karena `GET` wajib bersifat *safe* (tidak boleh mengubah *state*); Opsi B merusak pengalaman pengguna di jaringan seluler; Opsi D justru memperburuk latensi dan tidak mencegah *duplicate submission* apabila klien tetap mengirim dua permintaan. |
| **2** | **B** | **Benar:** **Webhook** bertanda tangan HMAC-SHA256 adalah standar industri untuk notifikasi asinkron satu arah dari *Payment Gateway* (FinPay); **gRPC** (HTTP/2 + Protobuf biner) unggul untuk komunikasi internal *east–west* berlatensi rendah antar-layanan; dan **REST** (JSON + OpenAPI) paling kompatibel, *cacheable*, dan mudah diintegrasikan untuk klien Mobile/Web serta mitra eksternal.<br/>*Mengapa opsi lain salah:* Opsi A terbalik menempatkan protokol eksternal/internal; Opsi C memboroskan sumber daya dengan *polling* 1 detik ke FinPay dan gRPC murni tidak didukung langsung browser tanpa *proxy*; Opsi D membawa beban kompleksitas SOAP *legacy* yang berat untuk aplikasi mobile. |
| **3** | **D** | **Benar:** *Polyglot Persistence* menempatkan setiap mesin sesuai kekuatan intinya: **PostgreSQL (ACID)** menjaga integritas finansial pesanan, reservasi, dan ledger poin; **MongoDB** mengakomodasi skema atribut heterogen 18.500 SKU; **Redis** mengeksekusi *cache* dan *atomic stock lock* sub-2 ms; **Elasticsearch** unggul untuk *full-text fuzzy search* dan *geo-distance* 120 toko.<br/>*Mengapa opsi lain salah:* Opsi A membebani satu mesin Document DB dengan pencarian teks dan transaksi ACID lintas entitas; Opsi B salah karena Elasticsearch bersifat *eventually consistent* dan bukan *system of record* finansial; Opsi C berisiko kehilangan seluruh data transaksi jika memori Redis *crash* tanpa persistensi ACID relasional. |
| **4** | **A** | **Benar:** Saat partisi jaringan (**P**) terjadi di luar Jawa, kasir fisik toko wajib memilih **AP** (*Local Outbox Queue* agar operasional antrean toko tidak lumpuh), sementara *checkout* online memakai **CP** (ACID + Redis lock) ditambah proteksi otomatis menonaktifkan *Click & Collect* untuk stok tipis di toko yang sedang *sync degraded* guna mencegah *overselling*.<br/>*Mengapa opsi lain salah:* Opsi B melumpuhkan penjualan 15 toko fisik dan memicu penolakan keras Store Ops; Opsi C keliru secara teoretis karena partisi jaringan (**P**) tidak dapat dihilangkan di jaringan terdistribusi lintas 24 kota; Opsi D mengembalikan masalah pembatalan *stockout* 11,4%. |
| **5** | **B** | **Benar:** Memaksakan 24 *microservices* pada 11 *developer* aktif (> 2 layanan per *engineer*) melanggar *Conway's Law* dan berisiko tinggi melahirkan ***Distributed Monolith***—lonjakan beban CI/CD, *debugging* terdistribusi, latensi jaringan berantai, biaya *cloud* melampaui CB-03, dan jadwal 14 Sprint molor. Solusi tepat adalah 5–6 *Right-Sized Domain Services* sesuai *Bounded Contexts*.<br/>*Mengapa opsi lain salah:* Opsi A keliru karena pemecahan berlebih justru menambah latensi jaringan dan biaya infrastruktur; Opsi C salah karena semakin banyak layanan justru membuat pengujian integrasi (SIT) makin kompleks; Opsi D keliru karena dekoupling *legacy* bergantung pada pola ACL, bukan jumlah *microservices*. |
| **6** | **C** | **Benar:** ***Transactional Outbox Pattern*** meniadakan *Dual-Write Problem* karena penulisan pesanan dan pencatatan *event* dilakukan di dalam **satu transaksi ACID PostgreSQL yang sama** (keduanya berhasil atau keduanya batal). Relay/CDC mengirim pesan dengan jaminan *at-least-once*, sehingga konsumen wajib **Idempotent**.<br/>*Mengapa opsi lain salah:* Opsi A (BFF) dan Opsi B (*Cache-Aside*) sama sekali tidak mengatasi ketidakonsistenan penulisan DB + broker; Opsi D menciptakan *chatty synchronous chain* yang rentan *cascading failure* jika salah satu server WMS DC sedang melambat. |
| **7** | **D** | **Benar:** Dalam transaksi terdistribusi lintas layanan dan pihak eksternal (FinPay), kegagalan di tahap hilir (*short-pick* toko) diselesaikan oleh **Saga Orchestrator** melalui rangkaian ***Compensating Transactions*** (membalik efek bisnis secara semantik: *auto-refund*, pengembalian poin, penyesuaian stok + audit, dan notifikasi).<br/>*Mengapa opsi lain salah:* Opsi A mustahil dilakukan karena FinPay eksternal tidak mendukung protokol 2PC dan 2PC merusak skalabilitas; Opsi B merusak pengalaman pelanggan dan melanggar SLA; Opsi C merusak jejak audit keuangan dan melanggar kepatuhan pembukuan. |
| **8** | **A** | **Benar:** Pola ***Circuit Breaker*** mendeteksi lonjakan kegagalan/latensi ERP lalu berpindah ke status **`Open`** (*fail-fast* ke *Fallback* agar *thread pool* OMS tidak habis), kemudian setelah *cooldown* masuk ke **`Half-Open`** untuk menguji pemulihan sebelum kembali **`Closed`**. *Exponential Backoff + Jitter* mencegah *retry storm*.<br/>*Mengapa opsi lain salah:* Opsi B justru mempercepat kehabisan *thread* OMS dan menciptakan *Self-Inflicted DDoS* terhadap ERP; Opsi C melanggar standar keamanan *Defense-in-Depth* tanpa memperbaiki latensi tutup buku ERP; Opsi D sama sekali tidak relevan dan merusak operasi 120 toko. |
| **9** | **B** | **Benar:** Batas *downtime* untuk 99,5% adalah $0{,}5\% \times 8.760 = \mathbf{43{,}8\text{ jam/tahun}}$ (~3,65 jam/bulan). Kombinasi **HA Multi-AZ Region Jakarta** (desain internal ≥ 99,9% = 8,76 jam/thn) + **DR *Warm Standby*** (RPO ≤ 5 mnt, RTO ≤ 30 mnt) + disiplin **FinOps** memenuhi seluruh target NFR, UU PDP, dan tepat masuk sisa pagu *cloud* Rp 420 jt dalam CB-03.<br/>*Mengapa opsi lain salah:* Opsi A salah hitung (52,56 menit adalah 99,99%), melampaui pagu CB-03 secara masif, dan berisiko melanggar transfer data lintas batas UU PDP; Opsi C salah hitung 10× lipat dan rentan kehilangan data; Opsi D salah hitung (4,38 jam adalah 99,95%) dan RPO 7 hari tidak dapat diterima untuk bisnis e-commerce bernilai Rp 300 M/tahun. |
| **10** | **C** | **Benar:** **Tokenisasi FinPay** menyingkirkan data kartu PAN/CVV dari infrastruktur SNR (menyusutkan lingkup PCI-DSS ke SAQ-A); **pemisahan tabel PII + anonimisasi/crypto-shredding** memenuhi *Right to Erasure* UU PDP sekaligus mempertahankan integritas pembukuan transaksi; dan **RBAC berbasis klaim JWT + validasi `store_code`** menutup tuntas kerentanan **OWASP API5 (BFLA)** serta **API1 (BOLA)**.<br/>*Mengapa opsi lain salah:* Opsi A fatal karena Base64 bukan enkripsi, menghapus baris `orders` merusak laporan pajak/akuntansi, dan *security by obscurity* mudah ditembus; Opsi B melanggar PCI-DSS, melanggar UU PDP, dan parameter `?is_staff=true` mudah dipalsukan klien; Opsi D melanggar hukum residensi UU PDP dan mematikan jejak audit forensik. |

---

## 10. Rangkuman, Glosarium, dan Referensi

### 10.1 Rangkuman

1. **Arsitektur adalah Seni *Trade-Off*:** Seorang *Senior Solution Architect* merancang sistem bukan untuk mengejar tren teknologi, melainkan memenuhi NFR bisnis (2.500 TPM, sync ≤ 60 detik, uptime ≥ 99,5%, UU PDP & PCI-DSS) di dalam batas kapasitas tim dan pagu anggaran (CB-02 Rp 1,65 M & CB-03 Rp 1,15 M).
2. **API Contract-First, Gateway & BFF:** Standar RESTful yang ketat—terutama header **`Idempotency-Key`** pada aksi mutasi, *cursor pagination*, OpenAPI 3.1 *Contract-First*, dan pemilihan protokol tepat (**REST** publik, **gRPC** internal, **Webhook** mitra)—dilindungi **API Gateway** (OAuth 2.0/OIDC/JWT, *rate limiting*, TLS 1.3) serta dioptimalkan lewat **BFF** (Mobile, Web, Store Ops).
3. **Polyglot Persistence & CAP Theorem:** Memadukan **PostgreSQL (ACID)**, **MongoDB**, **Redis** (*Cache-Aside/Write-Through* + *atomic lock*), dan **Elasticsearch** mencegah *bottleneck* basis data tunggal. Di bawah **CAP Theorem**, terapkan **CP** untuk transaksi stok/pembayaran online dan **AP (*Eventual Consistency*)** untuk operasi kasir lokal 120 toko agar toko tidak lumpuh saat internet terganggu.
4. **Right-Sized Services & Strangler Fig:** Hindari jebakan ***Distributed Monolith*** (*Premature Microservices*) dengan menyelaraskan jumlah layanan ke *Bounded Contexts* DDD dan *Conway's Law* (6 domain services untuk tim 18 personel PT NDS). Gunakan **Strangler Fig Pattern** + **Anti-Corruption Layer (ACL)** untuk migrasi bertahap tanpa mematikan ERP/POS lama.
5. **Integrasi *Event-Driven* & Ketahanan:** Pisahkan jalur kritis dari pekerjaan hilir menggunakan **Event Bus** + **Transactional Outbox** + **Idempotent Consumer** + **DLQ**. Lindungi setiap batas jaringan dengan **Circuit Breaker** (`Closed → Open → Half-Open`), **Retry + Exponential Backoff & Jitter**, serta kelola transaksi lintas domain dengan **Saga Orchestration + Compensating Transactions**.
6. **Cloud Multi-AZ, DR, FinOps, Security & Observability:** Bedakan **HA Multi-AZ** (ketahanan gangguan lokal, RPO = 0) dari **DR *Warm Standby*** (pemulihan bencana, RPO ≤ 5 mnt, RTO ≤ 30 mnt). Terapkan **FinOps** sejak Hari 1 agar bebas *Cloud Bill Shock*, bangun keamanan *Defense-in-Depth* (TLS 1.3, AES-256/KMS, tokenisasi FinPay, UU PDP, OWASP API Top 10), pantau dengan **3 Pilar Observability** (*Metrics, Structured Logs, Distributed Tracing*), dan kunci setiap keputusan strategis melalui **ADR**.

### 10.2 Glosarium

| Istilah Inggris | Padanan & Penjelasan dalam Bahasa Indonesia |
|-----------------|---------------------------------------------|
| **Anti-Corruption Layer (ACL)** | *Lapisan anti-korupsi* — lapisan adaptor penerjemah yang melindungi model domain sistem modern dari skema, protokol, atau struktur data usang sistem *legacy* |
| **API Gateway** | *Gerbang API* — titik masuk terpusat yang menangani autentikasi (OAuth 2.0/JWT), TLS termination, *rate limiting*, perutean trafik, dan pencatatan telemetri |
| **Architecture Decision Record (ADR)** | *Catatan keputusan arsitektur* — dokumen singkat berversi yang merekam konteks, alternatif opsi, keputusan final, dan *trade-off* suatu keputusan arsitektur penting |
| **Backend for Frontend (BFF)** | *Layanan penyangga khusus antarmuka klien* — lapisan agregasi API yang disesuaikan per jenis klien (Mobile, Web, Tablet Toko) agar payload efisien |
| **Bounded Context** | *Batas konteks domain* — batasan eksplisit dalam *Domain-Driven Design* (DDD) di mana model data dan istilah bisnis memiliki definisi serta kepemilikan tunggal |
| **Cache Stampede (*Thundering Herd*)** | *Serbuan serentak ke basis data* — kondisi lonjakan beban mendadak ke basis data akibat ribuan permintaan masuk bersamaan tepat saat entri *cache* populer kedaluwarsa |
| **CAP Theorem** | *Teorema CAP* — prinsip sistem terdistribusi yang menyatakan saat terjadi partisi jaringan (*Partition Tolerance*), sistem harus memilih antara *Consistency* atau *Availability* |
| **Circuit Breaker Pattern** | *Pola pemutus sirkuit* — mekanisme ketahanan yang memutus panggilan ke layanan bermasalah (*Open*) agar sistem cepat beralih ke *Fallback* dan mencegah efek domino |
| **Compensating Transaction** | *Transaksi kompensasi* — operasi pembalik secara semantik (mis. *auto-refund* atau pengembalian poin) pada pola *Saga* untuk membatalkan efek langkah terdahulu yang sudah sukses |
| **Contract-First API Design** | *Desain API berbasis kontrak terlebih dahulu* — praktik menyepakati spesifikasi OpenAPI/AsyncAPI sebelum menulis kode agar tim produsen dan konsumen dapat bekerja paralel memakai *Mock Server* |
| **Dead Letter Queue (DLQ)** | *Antrean pesan gagal* — antrean khusus untuk menampung pesan/event yang gagal diproses berulang kali agar tidak menyumbat antrean utama dan dapat diinvestigasi/diputar ulang |
| **Defense-in-Depth** | *Pertahanan berlapis* — strategi keamanan yang menerapkan kendali independen di setiap lapisan (Edge/WAF, jaringan, API, aplikasi, basis data, KMS, dan audit log) |
| **Disaster Recovery (DR)** | *Pemulihan bencana* — rencana, infrastruktur, dan prosedur teruji untuk memulihkan sistem dan data pasca-bencana besar sesuai target **RPO** dan **RTO** |
| **Distributed Monolith** | *Monolit terdistribusi* — *anti-pattern* sistem yang dipecah ke banyak layanan jaringan tetapi masih terikat erat (*tightly coupled*) sehingga mewarisi keburukan monolit sekaligus kerumitan terdistribusi |
| **Event-Driven Architecture (EDA)** | *Arsitektur berbasis kejadian* — pola integrasi asinkron di mana layanan saling berkomunikasi dengan menerbitkan dan mengonsumsi *event* fakta bisnis melalui *Message Broker* |
| **Eventual Consistency** | *Konsistensi akhir* — model konsistensi di mana replika data tidak selalu identik pada milidetik yang sama, tetapi dijamin konvergen menuju nilai yang sama dalam batas waktu tertentu (mis. ≤ 60 detik) |
| **FinOps** | *Tata kelola finansial operasional cloud* — disiplin kolaboratif tim teknologi dan keuangan untuk mengendalikan biaya *cloud* melalui *right-sizing*, *auto-scaling*, *tagging*, dan pengawasan anggaran |
| **High Availability (HA)** | *Ketersediaan tinggi* — rancangan redundansi aktif lintas *Availability Zone* untuk menjaga sistem tetap beroperasi hampir tanpa jeda ketika komponen lokal mengalami kegagalan |
| **Idempotency / Idempotency-Key** | *Sifat idempoten / kunci idempotensi* — jaminan bahwa eksekusi berulang atas permintaan yang sama (melalui kunci unik klien) menghasilkan *state* sistem yang identik tanpa efek ganda |
| **Observability (3 Pillars)** | *Keteramatan sistem* — kemampuan memahami kondisi internal sistem terdistribusi melalui integrasi **Metrics**, **Structured Logs**, dan **Distributed Tracing** |
| **Polyglot Persistence** | *Persistensi poliglot* — penggunaan beberapa jenis teknologi penyimpanan data (RDBMS, Document, Key-Value, Search Engine) yang disesuaikan dengan karakter beban tiap domain |
| **RPO (*Recovery Point Objective*)** | *Target titik pemulihan* — batas toleransi maksimum kehilangan data yang diukur dalam rentang waktu mundur sebelum bencana terjadi |
| **RTO (*Recovery Time Objective*)** | *Target waktu pemulihan* — batas toleransi maksimum durasi waktu sejak bencana terjadi hingga layanan kembali pulih beroperasi |
| **Saga Pattern** | *Pola Saga* — metode pengelolaan transaksi bisnis terdistribusi melalui rangkaian transaksi lokal antar-layanan dengan mekanisme kompensasi (*Choreography* atau *Orchestration*) |
| **Strangler Fig Pattern** | *Pola pohon ara pencekik* — strategi modernisasi sistem *legacy* secara bertahap dengan mengalihkan fungsi sedikit demi sedikit ke sistem baru hingga sistem lama dapat dipensiunkan dengan aman |
| **Transactional Outbox Pattern** | *Pola kotak keluar transaksional* — teknik menulis data bisnis dan pesan *event* dalam satu transaksi ACID basis data yang sama guna menghilangkan *Dual-Write Problem* |

### 10.3 Referensi

1. Richards, M., & Ford, N. (2020). *Fundamentals of Software Architecture: An Engineering Approach*. Sebastopol, CA: O'Reilly Media.
2. Newman, S. (2021). *Building Microservices: Designing Fine-Grained Systems* (2nd ed.). Sebastopol, CA: O'Reilly Media.
3. Hohpe, G., & Woolf, B. (2003). *Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions*. Boston, MA: Addison-Wesley.
4. Kleppmann, M. (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems* (DDIA). Sebastopol, CA: O'Reilly Media.
5. Amazon Web Services (AWS). (2024). *AWS Well-Architected Framework* (6 Pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability). Tersedia di: https://docs.aws.amazon.com/wellarchitected/
6. Google Cloud. (2024). *Google Cloud Architecture Framework & SRE Workbook*. Tersedia di: https://cloud.google.com/architecture/framework
7. OWASP Foundation. (2023). *OWASP API Security Top 10 (2023 Edition)*. Tersedia di: https://owasp.org/API-Security/
8. PCI Security Standards Council. (2024). *Payment Card Industry Data Security Standard (PCI-DSS) v4.0.1*.
9. OpenAPI Initiative. (2021). *OpenAPI Specification v3.1.0*. Tersedia di: https://spec.openapis.org/oas/latest.html
10. Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP).

---

## 11. Lampiran: Template Siap Pakai

### 11.1 Template Architecture Decision Record (ADR)

```markdown
#### ARCHITECTURE DECISION RECORD: ADR-[Nomor] — [Judul Singkat & Tegas]
- **Status:** [Proposed | Accepted | Deprecated | Superseded by ADR-XXX]
- **Tanggal:** [DD MMM YYYY]
- **Penyusun:** [Nama — Solution Architect]
- **Peninjau & Pemberi Persetujuan:** [CTO / Lead Architect / Security Lead / PM]
- **Keterkaitan Proyek / NFR:** [Mis. Proyek OMNI — Target 2.500 TPM, Pagu CB-03 Rp 1,15 M, UU PDP]

##### 1. Konteks & Pendorong Keputusan (Context & Architectural Drivers)
[Uraikan permasalahan bisnis/teknis secara objektif, angka NFR wajib, batasan anggaran, ukuran & kapabilitas tim, ketergantungan proyek paralel, serta tenggat waktu yang melatarbelakangi keputusan ini.]

##### 2. Opsi yang Dievaluasi (Options Considered)
| Dimensi Evaluasi | Opsi 1: [Nama Opsi] | Opsi 2: [Nama Opsi] | Opsi 3: [Nama Opsi — Terpilih] |
|------------------|---------------------|---------------------|--------------------------------|
| **Kelebihan Utama (Pro)** | [...] | [...] | [...] |
| **Kelemahan & Risiko (Kontra)** | [...] | [...] | [...] |
| **Kesesuaian NFR & Keamanan** | [Tinggi/Sedang/Rendah] | [Tinggi/Sedang/Rendah] | [Tinggi/Sedang/Rendah] |
| **Estimasi Dampak Biaya & Jadwal** | [Rp ... / ±X mgg] | [Rp ... / ±X mgg] | [Rp ... / ±X mgg] |
| **Kesesuaian Kapabilitas Tim** | [Sesuai/Berat] | [Sesuai/Berat] | [Sesuai/Berat] |

##### 3. Keputusan Final (Decision)
Kami memutuskan memilih **Opsi [X]: [Nama Opsi]** karena [alasan berbasis bukti & metrik prioritas utama].

##### 4. Konsekuensi, Trade-Off & Rencana Mitigasi (Consequences)
- **Dampak Positif:** [Daftar manfaat langsung yang diperoleh]
- **Trade-Off Negatif yang Diterima Secara Sadar:** [Kompleksitas/biaya tambahan yang tetap muncul]
- **Aksi Mitigasi & PIC:** [Langkah konkret menekan trade-off + penanggung jawab & target tanggal]
- **Pemicu Peninjauan Ulang (Revisit Trigger):** [Kondisi objektif di masa depan yang memicu evaluasi ulang ADR ini, mis. trafik > X TPM atau ukuran tim > Y engineer]
```

---

### 11.2 Template REST & Event API Contract Specification

```markdown
#### API & EVENT CONTRACT SPECIFICATION (CONTRACT-FIRST)
- **Nama Layanan / Domain:** [Mis. Inventory & Reservation Service] | **Versi Kontrak:** v1.0 (OpenAPI 3.1)
- **Pemilik Layanan (Provider):** [Tim/Vendor] | **Konsumen Utama (Consumers):** [Mobile BFF, OMS, POS Adapter]

##### A. Spesifikasi Endpoint REST
- **Endpoint & Metode:** `[GET/POST/PUT/PATCH/DELETE] /v1/[resources]/{id}`
- **Autentikasi & Otorisasi (RBAC/ABAC):** [OAuth 2.0 JWT / mTLS | Scope/Role wajib & cek kepemilikan anti-BOLA/BFLA]
- **Idempotency & Rate Limit:** [Wajib `Idempotency-Key`? Ya/Tidak | TTL 24 jam | Batas X req/menit/klien]
- **SLA Performa & Ketahanan:** [Latensi p95 <= X ms | Timeout Y dtk | Circuit Breaker Fallback: ...]

###### Contoh Request & Response JSON
- **Request Headers:** `Authorization`, `Idempotency-Key`, `X-Correlation-ID`, `Content-Type: application/json`
- **Request Body:** `{ ... }`
- **Success Response (`200/201/202`):** `{ ... }`

###### Matriks Kode Status & Penanganan Galat
| HTTP Status | Error Code Internal | Kondisi Pemicu | Aksi yang Disarankan bagi Klien |
|-------------|---------------------|----------------|---------------------------------|
| `400 / 422` | `VALIDATION_ERROR` | Payload tidak valid / aturan bisnis dilanggar | Jangan *retry*; tampilkan pesan validasi ke pengguna |
| `401 / 403` | `UNAUTHORIZED / FORBIDDEN` | Token kedaluwarsa atau peran/objek tidak berwenang | Refresh token (`401`) atau tolak akses (`403`) |
| `409` | `STATE_CONFLICT` | Stok habis / *optimistic lock mismatch* | Ambil ulang data terbaru & tawarkan alternatif |
| `429` | `RATE_LIMIT_EXCEEDED` | Melewati kuota trafik | Hormati header `Retry-After` + *backoff* |
| `503 / 504` | `DEPENDENCY_UNAVAILABLE` | Layanan hilir lambat atau *Circuit Breaker Open* | *Retry* terbatas (*Exponential Backoff + Jitter*) |

##### B. Spesifikasi Event Asinkron (Kafka / Cloud PubSub)
- **Nama Topik & Tipe Event:** `omni.[domain].events.v1` — `[domain].[entity].[past_tense_action]`
- **Partition Key:** `[Mis. {location_code}:{sku} — menjamin urutan kronologis]`
- **Garansi Pengiriman & Retensi:** [At-Least-Once via Transactional Outbox | Retensi topik X hari | Topik DLQ: `...dlq`]
- **Strategi Idempotent Consumer:** [Deduplikasi via `event_id` + verifikasi `sequence_number`]
- **Schema JSON Payload:** `{ "specversion": "1.0", "event_id": "...", "event_time": "...", "correlation_id": "...", "data": { ... } }`
```

---

### 11.3 Template Cloud Security, NFR & DR Readiness Matrix

```markdown
#### CLOUD ARCHITECTURE, SECURITY, NFR & DR READINESS MATRIX
- **Nama Proyek / Sistem:** [Isi Nama Proyek] | **Cloud Region Primer:** [Jakarta — AWS/GCP]
- **Tanggal Tinjauan Gate:** [DD MMM YYYY] | **Peninjau:** [CTO / InfoSec Lead / FinOps / QA Lead]

##### A. Verifikasi Non-Functional Requirements (NFR) & Kapasitas
| Kategori NFR | Metrik Target Bisnis | Target Desain Internal | Mekanisme Arsitektur Pengendali | Bukti Verifikasi (Uji Beban / Drill) | Status |
|--------------|----------------------|------------------------|----------------------------------|--------------------------------------|--------|
| **Throughput** | [Mis. 2.500 TPM] | [125 TPS burst / 3.600 RPS] | [HPA Auto-Scaling, Redis, Read Replicas] | [Laporan Load Test QA — Tanggal] | [ ] |
| **Latensi / Sync** | [Sync stok <= 60 dtk] | [p95 <= 25 dtk] | [Event Bus + Outbox + Cache Invalidation] | [Hasil SIT End-to-End 120 Toko] | [ ] |
| **Availability** | [>= 99,5% (43,8 jam/thn)] | [>= 99,9% (8,76 jam/thn)] | [Multi-AZ Active-Active (3 AZ) + Circuit Breaker] | [Simulasi Chaos / AZ Failover] | [ ] |
| **DR (RPO / RTO)** | [RPO <= 5 mnt; RTO <= 30 mnt] | [WAL Sync + Warm Standby] | [Immutable Backup + IaC Terraform Failover] | [Laporan DR Drill Teruji — Tanggal] | [ ] |

##### B. Matriks Kepatuhan Keamanan (Defense-in-Depth, UU PDP, PCI-DSS & OWASP)
| No | Domain Kendali Keamanan | Persyaratan Wajib | Implementasi Teknis | Status Audit InfoSec |
|----|-------------------------|-------------------|---------------------|----------------------|
| 1 | **Enkripsi In-Transit & At-Rest** | TLS 1.3 publik, mTLS internal, AES-256 KMS + PII field encryption | [...] | [Lulus/Belum] |
| 2 | **Residensi & Hak Subjek UU PDP** | Region Jakarta, Consent Log immutable, Data Export & PII Anonymization | [...] | [Lulus/Belum] |
| 3 | **Kepatuhan PCI-DSS** | 0 penyimpanan PAN/CVV (Tokenisasi/Hosted Fields via Payment Gateway) | [...] | [Lulus/Belum] |
| 4 | **OWASP API Security Top 10** | Anti-BOLA/BFLA (RBAC+UUID), Rate Limiting, WAF, Validasi Webhook HMAC | [...] | [Lulus/Belum] |
| 5 | **Observability & PenTest** | 3 Pilar (Metrics, JSON Logs anti-PII, OTel Tracing) & 0 Critical/High PenTest | [...] | [Lulus/Belum] |

##### C. Ringkasan Kendali FinOps & Pagu Anggaran Infrastruktur
- **Pagu Anggaran Disetujui:** Rp [X,XX] M | **Alokasi Non-Cloud (Perangkat/Audit):** Rp [X,XX] M | **Pagu Cloud:** Rp [X,XX] M
- **Proyeksi Burn Rate Bulanan:** Dev/Stg Rp [X] jt (Auto-Stop aktif) + Prod Multi-AZ & DR Rp [Y] jt = Total Rp [Z] jt/bln
- **Ambang Peringatan Otomatis (*Budget Alerts*):** 60% (Info SA) | 80% (Review PM/CTO) | 95% (Eskalasi CFO)
- **Persetujuan Go-Live Readiness:** Lead SA (__________) | CTO (__________) | Head of Legal & InfoSec (__________)
```
