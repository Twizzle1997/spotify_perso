<!DOCTYPE html>
<html lang="en">

% include('head.html', title = "Prairie - Bonus")

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

                    <!-- Sidebar Toggle (Topbar) -->
                    <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3">
                        <i class="fa fa-bars"></i>
                    </button>

                </nav>
                <!-- End of Topbar -->

                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <!-- Page Heading -->
                    <div class="d-sm-flex align-items-center justify-content-between mb-4">
                        <h1 class="h3 mb-0 text-gray-800">Bonus</h1>
                    </div>


                    <!-- Content Row -->

                    <div class="row">

                        <!-- Pie Chart -->
                        <div class="col-xl-4 col-lg-5">
                            <div class="card shadow mb-4 h-100">
                                <!-- Card Header - Dropdown -->
                                <div
                                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                                    <h6 class="m-0 font-weight-bold text-primary">Try the API</h6>
                                </div>
                                <form action="/bonus" method="POST" enctype="multipart/form-data">
                                    <div class="form-group d-flex flex-wrap">
                                        <input type="file" class="form-control-file" id="uploadfile" name="uploadfile">
                                        <input type="submit" value="Start upload" />
                                    </div>
                                </form>
                                <!-- Card Body -->
                                <div class="card-body">
                                    <figure>
                                        <figcaption>
                                            % if image_path != "":
                                            <img src="/img/tmp/{{image_path}}" class="img-fluid" alt="Image">
                                            % end
                                            {{image_path}}
                                        </figcaption>
                                    </figure>
                                </div>
                            </div>
                        </div>

                        <!-- Content Column -->
                        <div class="col-lg-8 mb-4">

                            <!-- Project Card Example -->
                            <div class="card shadow mb-4 h-100">
                                <div class="card-header py-3">
                                    <h6 class="m-0 font-weight-bold text-primary">Labels</h6>
                                </div>
                                <div class="card-body">
                                    % for desc, score in labels.items():
                                    <h4 class="small font-weight-bold">{{desc}} <span
                                            class="float-right">{{score}}</span></h4>
                                    <div class="progress mb-4">
                                        <div class="progress-bar bg-success" role="progressbar" style="width:{{score}}"
                                            aria-valuenow="{{score}}" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                    % end
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
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

</body>

</html>