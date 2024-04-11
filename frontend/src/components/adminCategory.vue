<template>
    <div class="categories-container">
      <b-navbar toggleable="lg" type="light" variant="light" class="gradient-nav">
        <b-navbar-brand  class="navbar-logo"><router-link to="/admin/dashboard">Shopzee</router-link></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  
        <b-collapse id="nav-collapse" is-nav>
          
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            
  
            <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
        <br>
        <b-button variant="primary" class="create-cat-btn" @click="$router.push('/cat_create')">Create Category</b-button>
            
      <b-row>
        
        <b-col v-for="cat in categories" :key="cat.id" md="4" class="category-card">
          <b-card 
            :title="cat.name"
            tag="article"
            class="category-card-inner"
          >
          <div class="category-image-container" >
            <img :src="getImageSrc(cat.image)" alt="Category Image" class="category-image" />
          </div>
            
            
            <b-card-text class="category-card-text">
              Description:  {{ cat.desc }}
            </b-card-text>
  
          <div class="button-row">
            <b-button variant="primary" class="view-products-btn" style="margin-right: 10px;" :to="`/cat_update/${cat.id}`">
              Edit Category</b-button>
          </div>
              <b-button type="button" variant="danger" @click="showDeleteConfirmation(cat)" style="margin-top: 10px;">
                  Delete Category
              </b-button>
           
          </b-card>
        </b-col>
      </b-row>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  import {mapActions} from 'vuex'
  export default {
      
    data() {
      return {
        categories: [],
        
      };
    },
    mounted() {
      this.getCategories();
      document.title='Admin Categories';
    },
    methods: {
      getImageSrc(imageData) {
              return `data:image/png;base64,${imageData}`
          },
      getCategories() {
        axios
          .get('http://127.0.0.1:5000/category',{
              headers: {
                  Authorization: localStorage.getItem('token')
              },
          })
          .then((response) => {
            this.categories = response.data
            // if(response.data.message==='Token is missing'){
            //   alert('Token is Missing');
            // }
          })
          .catch((error) => console.error('error :', error));
      },
      
      showDeleteConfirmation(category) {
        console.log(category);
        const confirmDelete = window.confirm(`Do you want to delete '${category.name}'?`);
        if (confirmDelete) {
          this.deleteCategory(category);
        }
      },
      ...mapActions({
              signOut: 'LOGOUT_ACTION'
          }),
        logout(){
          this.signOut()
        },
      
      deleteCategory(category) {
        const user = localStorage.getItem('user_type');
        const cat_id = category.id;
        if(user=='admin'){
        const apiurl = `http://127.0.0.1:5000/cat_delete/${cat_id}`;
  
        axios
          .post(apiurl)
          .then(() => {
            alert("Category Deleted Successfully")
            this.getCategories();
          })
          .catch((error) => {
            console.error(error);
            // Handle error, e.g., show an error message
          });
        }

        if(user=='storeManager'){
        const apiurl = `http://127.0.0.1:5000/store/cat_delete/${cat_id}`;
  
        axios
          .post(apiurl)
          .then(() => {
            alert("Category deletion sent for admin approval")
            this.getCategories();
          })
          .catch((error) => {
            console.error(error);
            // Handle error, e.g., show an error message
          });
        }
      },
      
    },
  };
  </script>
  
  <style scoped>
  /* General styles */
  .categories-container {
    padding: 0px;
    background-image: url("@/assets/dark.jpg");
    background-size: cover;
    background-position: center;
    min-height: 100vh;
  }
  
  .category-card-text {
    margin-top: 20px ;
    font-size: 18px;
    color: #000000;
  }
  
  .category-card {
    padding: 0 50px 0 50px;
    margin-bottom: 20px;
  }
  
  .button-row {
    display: flex;
    justify-content: space-between;
    /* align-items: center; */
    margin-top: 10px;
    
    
  }
  
  
  
  .category-image-container {
    width: 100%; 
    height: 200px; 
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .category-image {
    max-width: 100%;
    max-height: 100%;
  }
  
  .gradient-nav {
    background-image: linear-gradient(to right, rgb(255, 255, 255), rgb(255, 255, 255)), url("@/assets/card.jpeg");
    background-size: cover;
    background-position: center;
    color: white;
  }
  
  .navbar-logo {
    font-size: 24px;
    font-weight: bold;
    color: white;
  }
  
  .nav-item {
    font-size: 16px;
  }
  
  /* Search bar styles */
  .search-input {
    border-radius: 20px;
    border: none;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 8px 12px;
    color: #333;
  }
  
  .search-button {
    border-radius: 20px;
    margin-left: 10px;
    background-color: #007bff;
    color: white;
    font-weight: bold;
  }
  
  /* Login button styles */
  .login-button {
    border-radius: 20px;
    background-color: #f55;
    color: white;
    font-weight: bold;
  }
  
  .login-button a {
    color: white;
    text-decoration: none;
  }
  
  /* Category card styles */
  .category-card-inner {
    
    border: none;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
    background-image: url("@/assets/card.jpeg");
    background-size: cover;
    background-position: center;
  }
  
  .create-cat-btn {
    width: 25%;
    margin-top: 5px;
    margin-bottom: 25px;
    background-color: #ffffff;
    border: black;
    color:#000000;
  }
  
  
  .view-products-btn {
    width: 100%;
    margin-top: 10px;
    background-color: #008051;
    border: black;
  }
  
  .view-products-btn a {
    color: white;
    text-decoration: none;
  }
  
  .view-products-btn:last-child {
    margin-right: 0;
  }
  
  /* Media queries for responsiveness */
  @media screen and (max-width: 767px) {
    .category-card {
      flex: 0 0 100%;
      max-width: 100%;
    }
  }
  </style>
  