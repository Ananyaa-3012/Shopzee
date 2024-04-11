<template>
  <div class="category-products-container">
    <b-navbar toggleable="lg" type="danger" variant="info" class="gradient-nav">
      <b-navbar-brand  class="navbar-logo"><router-link to="/store/category">Shopzee</router-link></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          
          <b-button variant="secondary" class="search-button" to="/export">Export</b-button>
          <b-button variant="secondary" class="login-button" @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <br>
    <h1>Category: {{ category.name }}</h1>
    <div class="button-row">
          <b-button variant="primary" class="create-products-btn" :to="`/pdt_create/${category.id}`" >
            Create Product
          </b-button>
        </div>
        <b-row>

        </b-row>
      <div v-if="products.length>0">
        <b-row>
      <b-col v-for="product in products" :key="product.ID" md="4" class="product-card">
        <b-card
          :title="product.name"
          tag="article"
          class="product-card-inner"
          :class="{ 'out-of-stock': product.stock === 0 }">
        <div class="product-image-container">
          <img :src="getImageSrc(product.image)" alt="Product Image" class="product-image" />
        </div>
          <b-card-text class="category-card-text">
            Stock: {{ product.stock }} {{ product.unit }}
          </b-card-text>
          <b-card-text class="category-card-text">
            Date of Manufacture: {{ product.manufac }}
          </b-card-text>
          <b-card-text class="category-card-text">
            Date of Expiry: {{ product.expiry }}
          </b-card-text>
          <b-card-text class="category-card-text">
            Price: Rs.{{ product.price }}
          </b-card-text>

          <b-button variant="primary" class="view-products-btn" :to="`/pdt_update/${product.category}/${product.id}`">
          Edit Product</b-button>
          <b-button  variant="danger" @click="productDeleteConfirmation(product)" style="margin-top: 10px;">Delete Product</b-button>
        </b-card>
      </b-col>
    </b-row>
    </div>
    <div v-else>
      No products are there yet..... <br>
      <b-button variant="primary" to="/store/category" class="keep-shopping">Home</b-button>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import {mapActions} from 'vuex'

export default{
    
      data() {
        return {
          products: {},
          category: {}
        };
      },
      created() {
        this.getProducts();
        this.getCategory();
        document.title='Store-Product';
      },
      methods: {
        ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      },
        getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
        getProducts() {
            const cat_id = this.$route.params.cat_id;
            const apiurl = `http://127.0.0.1:5000/pdt_view/${cat_id}` 
            axios.get(apiurl,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.products=response.data;
            })
          .catch(error=> console.error('error :',error));
        },
        getCategory() {
            const cat_id = this.$route.params.cat_id;
            const apiurl = `http://127.0.0.1:5000/getCategory/${cat_id}` 
            axios.get(apiurl,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.category = response.data;
            })
          .catch(error=> console.error('error :',error));
        },
        productDeleteConfirmation(product) {
      const confirmDelete = window.confirm(`Do you want to delete '${product.name}'?`);
      if (confirmDelete) {
        this.deleteProduct(product);
      }
    },
    deleteProduct(product) {
      const productID = product.id;
      const apiurl = `http://127.0.0.1:5000/pdt_delete/${productID}`;

      axios
        .post(apiurl)
        .then(() => {
          this.getProducts();
        })
        .catch((error) => {
          console.error(error);
          // Handle error, e.g., shows an error message
        });
    },
      },
      
    
}
</script>

<style scoped>
/* General styles */
.category-products-container {
  padding: 0px;
  background-image: url("@/assets/dark.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.create-products-btn {
  width: 25%;
  margin: 10px;
  background-color: #ffffff;
  color:#000000;
}


.view-products-btn {
  width:75%;
  margin-top: 10px;
  background-color: #008051;
  border: black;
}

.category-card-text {
  font-size: 18px;
  color: #000000;
}

.view-products-btn a {
  color: white;
  text-decoration: none;
}

.product-image-container {
  width: 100%; 
  height: 200px; 
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-image {
  max-width: 100%;
  max-height: 100%;
}

.product-card {
  margin-bottom: 20px;
  padding: 0 50px 0 50px;
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
  color: #000000;
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

/* Product card styles */
.product-card-inner.out-of-stock {
  border: 2px solid red; /* Change border color for emphasis */
  opacity: 0.7; /* Reduce opacity to visually indicate out-of-stock */
}

.keep-shopping{
    box-align: center; 
    border-radius: 15px; 
    background-color: rgb(10, 110, 85);
    margin: 15px;
  }
  .keep-shopping:hover{
        background-color: white;
        color:#000000;  
  }

/* Media queries for responsiveness */
@media screen and (max-width: 767px) {
  .product-card {
    flex: 0 0 100%;
    max-width: 100%;
  }
}
</style>