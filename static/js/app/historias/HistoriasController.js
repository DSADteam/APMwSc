scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VHistorias/:idPila', {
                controller: 'VHistoriasController',
                templateUrl: 'app/historias/VHistorias.html'
            }).when('/VCrearHistoria/:idPila', {
                controller: 'VCrearHistoriaController',
                templateUrl: 'app/historias/VCrearHistoria.html'
            }).when('/VHistoria/:idHistoria', {
                controller: 'VHistoriaController',
                templateUrl: 'app/historias/VHistoria.html'
            });
});

scrumModule.controller('VHistoriasController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'ngTableParams', 'accionService', 'actorService', 'historiasService', 'objetivoService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, ngTableParams, accionService, actorService, historiasService, objetivoService, prodService) {
      $scope.msg = '';
      historiasService.VHistorias({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var VHistoria0Data = $scope.res.data0;
              if(typeof VHistoria0Data === 'undefined') VHistoria0Data=[];
              $scope.tableParams0 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VHistoria0Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VHistoria0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VCrearHistoria1 = function(idPila) {
        $location.path('/VCrearHistoria/'+idPila);
      };
      $scope.VProducto2 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };

      $scope.VHistoria0 = function(idHistoria) {
        $location.path('/VHistoria/'+((typeof idHistoria === 'object')?JSON.stringify(idHistoria):idHistoria));
      };

    }]);
scrumModule.controller('VCrearHistoriaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'accionService', 'actorService', 'historiasService', 'objetivoService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, accionService, actorService, historiasService, objetivoService, prodService) {
      $scope.msg = '';
      $scope.fHistoria = {};

      historiasService.VCrearHistoria({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistorias0 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VCrearActor2 = function(idPila) {
        $location.path('/VCrearActor/'+idPila);
      };
      $scope.VCrearAccion3 = function(idPila) {
        $location.path('/VCrearAccion/'+idPila);
      };
      $scope.VCrearObjetivo4 = function() {
        $location.path('/VCrearObjetivo');
      };

      $scope.fHistoriaSubmitted = false;
      $scope.ACrearHistoria1 = function(isValid) {
        $scope.fHistoriaSubmitted = true;
        if (isValid) {
          
          historiasService.ACrearHistoria($scope.fHistoria).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
scrumModule.controller('VHistoriaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'accionService', 'actorService', 'historiasService', 'objetivoService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, accionService, actorService, historiasService, objetivoService, prodService) {
      $scope.msg = '';
      $scope.fHistoria = {};

      historiasService.VHistoria({"idHistoria":$routeParams.idHistoria}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistorias0 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VCrearActor2 = function(idPila) {
        $location.path('/VCrearActor/'+idPila);
      };
      $scope.VCrearAccion3 = function(idPila) {
        $location.path('/VCrearAccion/'+idPila);
      };
      $scope.VCrearObjetivo4 = function() {
        $location.path('/VCrearObjetivo');
      };

      $scope.fHistoriaSubmitted = false;
      $scope.AModifHistoria1 = function(isValid) {
        $scope.fHistoriaSubmitted = true;
        if (isValid) {
          
          historiasService.AModifHistoria($scope.fHistoria).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
