<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <title>Dashboard::HostAware</title>
    <!-- ======= Styles ====== -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
    <link rel="apple-touch-icon" sizes="57x57" href="../static/css/favicon/apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="../static/css/favicon/apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="../static/css/favicon/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="../static/css/favicon/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="../static/css/favicon/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="../static/css/favicon/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="../static/css/favicon/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="../static/css/favicon/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../static/css/favicon/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192" href="../static/css/favicon/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="../static/css/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="../static/css/favicon/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="../static/css/favicon/favicon-16x16.png">
    <link rel="manifest" href="../static/cssfavicon/manifest.json">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="msapplication-TileImage" content="../static/css/favicon/ms-icon-144x144.png">
    <meta name="theme-color" content="#ffffff">
</head>

<body>
    <!-- =============== Navigation ================ -->
    <div class="container">
        <div class="navigation">
            <ul>
                <li>
                    <a href="#">
                        <span class="icon">
                            <ion-icon name='logo-slack'></ion-icon>
                        </span>
                        <span class="title">HOST AWARE</span>
                    </a>
                </li>

                <li>
                    <a href="#">
                        <span class="icon">
                            <ion-icon name="home-outline"></ion-icon>
                        </span>
                        <span class="title">Dashboard</span>
                    </a>
                </li>

                <li>
                    <a href={{ url_for('settings') }}>
                        <span class="icon">
                            <ion-icon name="settings-outline"></ion-icon>
                        </span>
                        <span class="title">Settings</span>
                    </a>
                </li>

                <li>
                    <a href={{ url_for('login') }}>
                        <span class="icon">
                            <ion-icon name="log-out-outline"></ion-icon>
                        </span>
                        <span class="title">Sign Out</span>
                    </a>
                </li>
            </ul>
        </div>

        <!-- ========================= Main ==================== -->
        <div class="main">
            <div class="topbar">
                <div class="toggle">
                    <ion-icon name="menu-outline"></ion-icon>
                </div>

                <div class="user">
                    <img src="assets/imgs/hostaware-logo.png" alt="DisplayPicture">
                </div>
            </div>

            <!-- ======================= pie chart ================== -->

            <div class="cardBox">
                <div class="card">
                    <h2>Open Ports:</h2>
                    <ul>
                        {% for port in open_ports %}
                        <li>{{ port }}</li>
                        {% endfor %}
                    </ul>
                </div>
                <div class="card">
                        <ul>
                            <table>
                                   <tr>
                                      <th>Source IP</th>
                                      <th>Destination Port</th>
                                      <th>Source Port</th><br>
                                   </tr>
                                   <tr>
                                       <td>139.59.4.123</td>
                                       <td>34</td>
                                       <td>51116</td>
                                  </tr>
                            </table>
                        </ul>
                </div>
                <div class="card">
                    <h2>Alert Ports:</h2>
                    <br>
                    <ul>
                        li>22</li><br>
                    </ul>
                </div>
                <div class="alert">
                    <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                    WARNING : Some ports are been affected.
                </div> 
            </div>

            <!-- ================ Order Details List ================= -->
            <div class="details">
                <div class="Requests">
                    <div class="cardHeader">
                        <h2>Requests</h2>
                    </div>

                    <table>
                        <thead>
                            <tr>
                                <td>Source IP</td>
                                <td>Source Port</td>
                                <td>Status</td>
                            </tr>
                        </thead>

                        <tbody>
                            <tr>
                                <td>139.59.4.12.32</td>
                                <td>51116</td>
                                <td><span class="status delivered">Safe</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>


                <!-- =========== Scripts =========  -->
                <script src="../static/css/js/main.js"></script>

                <!-- ====== ionicons ======= -->
                <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
                <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
</body>

</html>
