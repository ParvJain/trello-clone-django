(function() {
  'use strict';

  angular
    .module('app.controller', [])
    .controller('Kanban', Kanban);

  Kanban.$inject = ['$scope'];

  function Kanban($scope) {

    $scope.groups = [
      {
        name: 'Group A',
        items: [{name: 'Item A'},{name: 'Item B'},{name: 'Item C'},{name: 'Item D'}]
      },
      {
        name: 'Group B',
        items: [{name: 'Item 1'},{name: 'Item 2'},{name: 'Item 3'},{name: 'Item 4'}]
      },
      {
        name: 'Group B',
        items: [{name: 'Item 1'},{name: 'Item 2'},{name: 'Item 3'},{name: 'Item 4'}]
      },
      {
        name: 'Group B',
        items: [{name: 'Item 1'},{name: 'Item 2'},{name: 'Item 3'},{name: 'Item 4'}]
      },
      {
        name: 'Group B',
        items: [{name: 'Item 1'},{name: 'Item 2'},{name: 'Item 3'},{name: 'Item 4'}]
      },
      {
        name: 'Group B',
        items: [{name: 'Item 1'},{name: 'Item 2'},{name: 'Item 3'},{name: 'Item 4'}]
      },
    ];


    $scope.$on('nested-bag.drop', function(e, el, container, source, sibling) {
      console.log(sibling.scope());
      console.log(container.scope());
    });

  }
})();
