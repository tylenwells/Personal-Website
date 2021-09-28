// Define the 'getpostsApp' module
var getpostsApp = angular.module('getpostsApp', []);

// Define the 'PostController' controller on the 'getpostsApp' module
getpostsApp.controller('PostController', function PostController($scope) {
    $scope.posts = [
        // I will eventually create a rest api server that i can deploy internally to access this data dynamically. for now I'm adding static entries. 
        {
            id: "0",
            title: "The Master Plan",
            description: "The plan for implementation of this site, including what solution are planned, etc.",
            timetoread: "5 minutes",
            content: "This is placeholder text to make sure that the Angular is working properly. asdf asdf asdf asdf asd fasdf asdfasd fasdf asdf asdqery qwefqwef qwerfq wetr qtq wertqwe tqwerqwe qert",
        },
        {
            id: "1",
            title: "The Master Plan",
            description: "The plan for implementation of this site, including what solution are planned, etc.",
            timetoread: "5 minutes",
            content: " MODAL # 2 This is placeholder text to make sure that the Angular is working properly. asdf asdf asdf asdf asd fasdf asdfasd fasdf asdf asdqery qwefqwef qwerfq wetr qtq wertqwe tqwerqwe qert",
        }
    ];
});