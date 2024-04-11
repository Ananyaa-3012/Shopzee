<template>
  <div class="categories-container">
    <b-navbar toggleable="lg" type="light" variant="dark" class="gradient-nav">
      <b-navbar-brand  class="navbar-logo"><router-link to="/home">Shopzee</router-link></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form @submit="onSubmit">
            <b-form-input v-model="form.query" class="search-input" placeholder="Search"></b-form-input>
            <b-button class="search-button" type="submit">Search</b-button>
          </b-nav-form>
          <b-button class="cart-button" to="/user/profile">Profile</b-button> 
          <b-button class="cart-button" variant="primary" to="/cart">Cart</b-button>
          <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
      <br>
    <b-row v-if="categories.length > 0">
      <b-col v-for="cat in categories" :key="cat.id" md="4" class="category-card">
        <b-card
          :title="cat.name"
          :title-tag="'h2'"
          class="category-card-inner"
          tag="article"
          style="font-weight: bold;"
        >

        <div class="category-image-container">
          <img :src="getImageSrc(cat.image)" alt="Category Image" class="category-image" />
        </div>
          
          
          
        
          <b-card-text class="category-card-text">
            Description:  {{ cat.desc }}
          </b-card-text>
          

          <b-button variant="primary" class="view-products-btn" :to="`/products/${cat.id}`">
            View Products
          </b-button>
        </b-card>
      </b-col>
    </b-row>
    <div v-else>
      <p><b>No categories exist</b></p>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import {mapActions} from 'vuex'

export default {
  data() {
    return {
      categories: [],
      form: {
        query: ''
      }
    };
  },
  mounted() {
    this.category();
    document.title='Dashboard';
  },
  methods: {
    getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },

    category() {
      axios
        .get('http://127.0.0.1:5000/user/category',{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
        .then((response) => {
          this.categories = response.data;
           
        })
        .catch((error) => console.error('error:', error));
        
    },
    onSubmit(event) {
        event.preventDefault()
        this.$router.push(`/search/${this.form.query}`);
       
      },
      ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      }
    
  }
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

.category-card {
  margin-bottom: 20px;
  padding: 0 50px 0 50px;
}

.b-card-title {
  font-weight: bold;
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

.nav-item a{
  color: black;
  text-decoration: none;
}

.gradient-nav {
  background-image: url("@/assets/card.jpeg");
  background-size: cover;
  background-position: center;
  color: white;
}

.navbar-logo {
  font-size: 24px;
  font-weight: bold;
}

.nav-item {
  font-size: 16px;
}

.cart-button {
  border-radius: 20px;
  border-color: none;
  background-color: rgb(10, 110, 85);
  color: white;
  font-weight: bold;
}

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
  margin-right: 10px;
  background-color: #007bff;
  color: white;
  font-weight: bold;
}

/* Login button styles */
.login-button {
  margin-left: 10px;
  margin-right: 10px;
  border-radius: 20px;
  background-color: #f55;
  color: white;
  font-weight: bold;
}

.login-button a {
  color: white;
  text-decoration: none;
}


.category-card-inner {
  border: none;
  border-radius: 10px;
  box-shadow: 0px 8px 16px rgb(0, 0, 0);
  background-image: url("@/assets/card.jpeg");
  background-size: cover;
  font-weight: bold;
  background-position: center;
}

.category-card-text {
  margin: 10px;
  font-size: 18px;
  color: #000000;
}

.view-products-btn {
  width: 100%;
  margin-top: 10px;
  background-color: #007bff;
}

.view-products-btn a {
  color: white;
  text-decoration: none;
}


@media screen and (max-width: 767px) {
  .category-card {
    flex: 0 0 100%;
    max-width: 100%;
  }
}
</style>