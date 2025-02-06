<?php
    session_start();

    if (!isset($_SESSION['username'])){ 
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <!--    <link href="images/logo.jpg" rel="shortcut icon"> -->
    <title> petrodo</title>
    
    <!-- core CSS -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/animate.min.css" rel="stylesheet">
    <link href="css/prettyPhoto.css" rel="stylesheet">  
    <link href="css/main.css" rel="stylesheet">
    <link href="css/responsive.css" rel="stylesheet">

</head><!--/head-->
        
<!--*********************************************START OF NAVIGATION BAR****************************************--> 
<body>
          
      <nav class="navbar navbar-inverse" role="banner">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a href="index.php"><h4 class="wow fadeInDown" style="margin-top:20px; color:Pink;">
                        <!--      <img src="images/logo.jpg"  width="15% "/> --> E-Petmarket</h4></a>
                </div>
    
                <div class="collapse navbar-collapse navbar-right wow fadeInDown">
                    <ul class="nav navbar-nav">
                         <li><a href="index.php"><i class="fa fa-home"></i>Home</a></li>
                        <li ><a href="about-us.php">About Us</a></li>
                        <li ><a href="available.php">Available Products</a></li>
                        <li class="active"><a href="contacts.php">Contacts</a></li>
                        <li class="active"><a href="search.php">search</a></li>
                                                          
                    </ul>
                </div>
            </div><!--/.container-->
        </nav><!--/nav-->
<!--*********************************************START OF CONTACT INFO****************************************-->
<body>
    <div class="container">
        <h1>Pet Breed Information</h1>
        <input type="text" id="searchInput" placeholder="Enter a pet breed (e.g., Golden Retriever)">
        <button onclick="searchBreed()">Search</button>
        <div id="result"></div>
    </div>
    <script>
        const breedData = [
            { breed: 'Labrador', nature: 'Outgoing, Even Tempered, Gentle', available_count:'available: 15pcs', images: 'lab.jpeg' },
            { breed: 'German Shepherd', nature: 'Loyal, Courageous, Confident',available_count:'available: 25pcs', images: 'R.jpeg' },
            { breed: 'Golden Retriever', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 10pcs', images: 'gold.jpeg' },
            { breed: 'French bulldog', nature: 'Friendly, very affectionate, family-oriented',available_count:'available: 3pcs', images: 'd11.jpg' },
            { breed: 'Poodle', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 5pcs', images: 'd3.jpg' },
            { breed: 'Bulldog', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 15pcs', images: '3.jpg' },
            { breed: 'Rottweiler', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 4pcs', images: 'rt.jpeg' },
            { breed: 'Beagle', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 2pcs', images: 'a7.jpg' },
            { breed: 'Daschund', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 4pcs', images: 'd6.jpg' },
            { breed: 'German shorthaired pointer', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 1pcs', images: 'dd.jpeg' },
            { breed: 'Pembroke Welsh corgi', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 2pcs', images: 'ch.jpeg' },
            { breed: 'Australian shepherd', nature: 'Friendly, Intelligent, Devoted',available_count:'available: unavailable', images: 'au.jpg' },
            { breed: 'Yorkshire terrier', nature: 'Friendly, Intelligent, Devoted',available_count:'available: unavailable', images: 'dog2.jpg' },
            { breed: 'Cavalier King Charles spaniel', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 3pcs', images: 'sp.jpeg' },
            { breed: 'Doberman', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 2pcs', images: 'db.jpg' },
            { breed: 'Boxer', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 6pcs', images: 'd1.jpg' },
            { breed: 'Miniature schnauzer', nature: 'Friendly, Intelligent, Devoted',available_count:'available: unavailable', images: 'd9.jpg' },
            { breed: 'Cane corso', nature: 'Friendly, Intelligent, Devoted',available_count:'available: unavailable', images: 'w.jpg' },
            { breed: 'Great Dane', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 1pcs', images: 't.jpeg' },
            { breed: 'Shih Tzu', nature: 'Friendly, Intelligent, Devoted',available_count:'available: 2pcs', images: '8.jpg' },
            // Add more dog breeds...

            // Cats
            { breed: 'Persian Cat', nature: 'Quiet, Sweet, Gentle', images: 'c9.jpg' },
            { breed: 'Maine Coon', nature: 'Adaptable, Intelligent, Gentle', image: 'maine_coon.jpg' },
            { breed: 'Siamese Cat', nature: 'Social, Playful, Vocal', image: 'siamese_cat.jpg' },
            {breed: 'Ragdoll', nature: 'Quiet, Sweet, Gentle', images: 'c81.jpg' },
            { breed: 'Main coon cat', nature: 'Quiet, Sweet, Gentle', image: 'persian_cat.jpg' },
            { breed: 'Devon Rex', nature: 'Quiet, Sweet, Gentle', image: 'persian_cat.jpg' },
            { breed: 'Exotic shorthair', nature: 'Quiet, Sweet, Gentle', image: 'persian_cat.jpg' },
            { breed: 'Abyssinian', nature: 'Quiet, Sweet, Gentle', image: 'persian_cat.jpg' },
            { breed: 'Sphynx', nature: 'Quiet, Sweet, Gentle', image: 'persian_cat.jpg' },
            { breed: 'Siberian', nature: 'Quiet, Sweet, Gentle', image: 'persian_cat.jpg' },
            // Add more cat breeds...

            // Birds
            { breed: 'Budgerigar (Budgie)', nature: 'Social, Playful, Intelligent', image: 'budgerigar.jpg' },
            { breed: 'Cockatiel', nature: 'Affectionate, Playful, Vocal', image: 'cockatiel.jpg' },
            { breed: 'African Grey Parrot', nature: 'Intelligent, Social, Talkative', image: 'african_grey_parrot.jpg' },
            // Add more bird breeds...

            // Fishes
            { breed: 'Goldfish', nature: 'Social, Hardy, Peaceful', images: 'f3.jpg' },
            { breed: 'Betta Fish', nature: 'Colorful, Aggressive, Labyrinth Organ', images: 'g23.png' },
            { breed: 'Angelfish', nature: 'Elegant, Graceful, Sociable', images: 'f2.jpg' },
            // Add more fish breeds...
        ];

        function searchBreed() {
            const searchInput = document.getElementById('searchInput');
            const resultDiv = document.getElementById('result');
            const breedName = searchInput.value.trim().toLowerCase();

            const matchingBreeds = breedData.filter(breed => breed.breed.toLowerCase() === breedName);

            if (matchingBreeds.length > 0) {
                const breed = matchingBreeds[0];
                const breedInfo = `
                    <h2>${breed.breed}</h2>
                    <p>Nature: ${breed.nature}</p>
                    <h2>${breed.available_count}</h2>
                    <img src="images/breeds/${breed.images}" alt="${breed.breed}" style="max-width: 1000%; height:1000%;">
                `;
                resultDiv.innerHTML = breedInfo;
            } else {
                resultDiv.innerHTML = '<p>Breed not found</p>';
            }
        }
    </script>
<!--*************************************************** FOOTERS **********************************************-->

<?php include('includes/footer.php');?><!--/#footer-->
    <?php include('loginModal.php')?>
    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/jquery.prettyPhoto.js"></script>
    <script src="js/jquery.isotope.min.js"></script>
    <script src="js/main.js"></script>
    <script src="js/wow.min.js"></script>
</body>
</html>

<?php 

} else if(isset($_SESSION['username'])) { 

    include('includes/admin.php');

} ?>