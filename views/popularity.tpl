<!DOCTYPE html>
<html lang="en">

% include('head.html', title = "Popularity")

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

        <!-- Sidebar -->
        % include('sidebar.tpl', compagny=compagny)
        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <!-- Topbar -->
                <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">
                    {{project}}
                </nav>
                <!-- End of Topbar -->

                <!-- Begin Page Content -->
                <form action="/popularity" method="post">
                    <div class="container-fluid">

                        <!-- Page Heading -->
                        <div class="d-sm-flex align-items-center justify-content-between mb-4">
                            <h1 class="h3 mb-0 text-gray-800">Prédiction de la popularité</h1>
                        </div>

                        <!-- Content Row -->
                        <div class="row">

                            <div class="col-xl-6 col-md-6 col-mb-6">
                                <div class="card shadow h-100 py-2 border-left-primary">
                                    <div class="card-body">
                                        <div class="row no-gutters align-items-center">
                                            <div class="col mr-2">
                                                <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                                    Sélection de la piste</div>
                                                <div class="h5 mb-0 font-weight-bold text-gray-800">
                                                    <select class="form-control mb-2" id="track" name="track">
                                                        % for item in tracks.itertuples():
                                                        <option value="{{item.track_id}}">{{item.name}}</option>
                                                        % end
                                                    </select>
                                                    <button value="Login" type="submit" title="lancer la recherche">
                                                        <i class="fas fa-search"></i>
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- /.container-fluid -->

                            <!-- Content Row -->

                            <!--<div class="row">-->

                            <!-- Area Chart -->
                            <div class="col-xl-6 col-lg-6 col-md-6">
                                <div class="card shadow mb-h-100 py-2">
                                    <!-- Card Header - Dropdown -->
                                    <div
                                        class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                                        <h6 class="m-0 font-weight-bold text-primary">Popularité estimée de la musique
                                            (%)</h6>
                                    </div>
                                    <!-- Card Body -->
                                    <div class="card-body">
                                        <div class="chart-area">
                                            <h4 class="small font-weight-bold">Popularité estimée : {{prediction}}</h4>
                                            <h4 class="small font-weight-bold">Popularité réelle : {{real_pop}}</h4>

                                            <div
                                                style="width: 100%;border-radius: 25px;border: 3px solid #858796; z-index: 7; background-color: #4e73df;">
                                                <div class="card-body"
                                                    style="border-radius: 20px; width: {{prediction}}%; z-index: 6;"
                                                    id="predictionBar">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- Content Row -->
                    </div>

                    <!-- End of Main Content -->

                    <!-- Footer -->
                    % include('footer.tpl', copyrights=copyrights)
                    <!-- End of Footer -->

            </div>
            <!-- End of Content Wrapper -->

        </div>
        <!-- End of Page Wrapper -->

        <!-- Scroll to Top Button-->
        <a class="scroll-to-top rounded" href="#page-top">
            <i class="fas fa-angle-up"></i>
        </a>

        % include('dependances.html')

        <script type="text/javascript">
            var barre = document.getElementById("predictionBar");
            var value = parseInt({{ prediction }});
            console.log(value);
            if (value > 80)
                barre.style.background = "#1cc88a";
            else if (value > 60)
                barre.style.background = "#36b9cc";
            else if (value > 40)
                barre.style.backgroundColor = "#4e73df";
            else if (value > 20)
                barre.style.backgroundColor = "#f6c23e";
            else if (value > 0)
                barre.style.backgroundColor = "#e74a3b";
        </script>

</body>

</html>