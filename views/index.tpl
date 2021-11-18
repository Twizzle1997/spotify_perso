<!DOCTYPE html>
<html lang="en">

% include('head.html', title = "Dashboard")

<body id="page-top">

  <!-- Page Wrapper -->
  <div id="wrapper">

    <!-- Sidebar -->
    % include('sidebar.tpl', compagny=compagny)

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
        <div class="container-fluid">

          <!-- Page Heading -->
          <div class="d-sm-flex align-items-center justify-content-between mb-4">
            <h1 class="h3 mb-0 text-gray-800">Dashboard - Music Consumption Stats</h1>
          </div>

          <div class="row">

            % include('smallCard.tpl', title="Temps moyen des morceaux", content="{} {}".format(avgtimesong, '(min)'))
            % include('smallCard.tpl', title="Temps Max des morceaux", content="{} {}".format(maxtimesong,  '(min)'))
            % include('smallCard.tpl', title="Temps Min des morceaux", content="{} {}".format(mintimesong, '(min)'))
            % include('smallCard.tpl', title="Nombre de morceaux dans plusieurs playlists", content=countsongs)

          </div>


          <!--
          <div class="col-lg-12">
            <div class="card shadow mb-4">

              <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Temps moyen des morceaux</h6>
                <h6 class="m-0 font-weight-bold text-primary">Temps Max des morceaux</h6>
                <h6 class="m-0 font-weight-bold text-primary">Temps Min des morceaux</h6>
                <h6 class="m-0 font-weight-bold text-primary">Nombre de morceaux dans plusieurs playlists</h6>
              </div>

              <div class="card-body py-3 d-flex flex-row align-items-center justify-content-around">
                <h4>{{avgtimesong}} (min)</h4>
                <h4>{{maxtimesong}} (min)</h4>
                <h4>{{mintimesong}} (min)</h4>
                <h4>{{countsongs}}</h4>
              </div>
            </div>
          </div>
          -->

          <!-- Aera Chart -->
          <div class="col-lg-12">
            <div class="card shadow mb-4">
              <div class="card-header py-3">
                <h6 class="m-0 font-weight-bold text-primary">Nombre de musiques par artiste</h6>
              </div>
              <div class="card-body">
                <table class="table table-bordered table-hover dt-reponsive nowrap" id="dataTable" cellspacing="0">
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>Nombre de pistes</th>
                    </tr>
                  </thead>
                  <tfoot>
                    <tr>
                      <th>Name</th>
                      <th>Nombre de pistes</th>
                    </tr>
                  </tfoot>
                  <tbody>
                    % for iteration in count_songs_by_artist:
                    <tr>
                      <td>{{iteration[0]}}</td>
                      <!-- <td>{artist{'id'}}</td> -->
                      <td>{{iteration[1]}}</td>
                    </tr>
                    % end
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- Area Chart -->
          <div class="col-lg-12">
            <div class="card shadow mb-4">
              <!-- Card Header - Dropdown -->
              <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Nombre de chansons par artiste</h6>
              </div>
              <!-- Card Body -->
              <div class="card-body">
                <div style="overflow-x: auto">
                  <img src="/get/data/artists">
                </div>
              </div>
            </div>
          </div>

          <!-- Area Chart -->
          <div class="col-lg-12">
            <div class="card shadow mb-4">
              <!-- Card Header - Dropdown -->
              <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Nombre de chansons par playlist</h6>
              </div>
              <!-- Card Body -->
              <div class="card-body">
                <div style="overflow-x: auto">
                  <img src="/get/data/playlist">
                </div>
              </div>
            </div>
          </div>

          <!-- Area Chart -->
          <div class="col-lg-12">
            <div class="card shadow mb-4">
              <!-- Card Header - Dropdown -->
              <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Nombre de chansons par bpm</h6>
              </div>
              <!-- Card Body -->
              <div class="card-body">
                <div style="overflow-x: auto">
                  <img src="/get/data/bpm">
                </div>
              </div>
            </div>
          </div>

          <!-- Area Chart -->
          <div class="col-lg-12">
            <div class="card shadow mb-4">
              <!-- Card Header - Dropdown -->
              <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Relation entre l'intensité et l'énergie
                </h6>
              </div>
              <!-- Card Body -->
              <div class="card-body">
                <div style="overflow-x: auto; text-align:center">
                  <img src="/get/data/intensity">
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

  <!-- DEPENDANCES -->
  % include('dependances.html')

</body>

</html>