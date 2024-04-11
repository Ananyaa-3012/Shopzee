<template>
  <div class="categories-container">
    <b-navbar type="light" class="gradient-nav">
      <b-navbar-brand class="navbar-logo" to="'/home'">Shopzee</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/home" class="nav-item">Home</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    
    <div class="user-info" >
      <h2>Welcome, {{ user.name }}</h2>
      <p><b>Email: </b>{{ user.email }}</p>
      <p><b>Address: </b>{{ user.address }}</p>
    </div>

    <h2 class="user-tickets-heading">Your Orders</h2>
<div v-if="orders.length>0">
    <div class="orders-container">
      <b-card v-for="(order, index) in orders" :key="index" class="order-card">
        <b-card-header>
          Order Time: {{ order[0].time }}
        </b-card-header>
        <b-table :items="order" :fields="fields" class="order-table">
          <template v-slot:cell(product)="data">
            {{ data.value }}
          </template>
          <template v-slot:cell(quantity)="data">
            {{ data.value }}
          </template>
          <template v-slot:cell(amount)="data">
            {{ data.value }}
          </template>
        </b-table>
        <div class="total-amount">
        Total Amount: {{ calculateTotalAmount(order) }}
      </div>
      </b-card>
    </div>
  </div>
  <div v-else>
    <h3>No Orders Yet</h3>
  </div>
  </div>
</template>


<script>
import axios from 'axios'
import {mapActions} from 'vuex'



export default {

    data(){
        return{
            user:[],
            orders:[],
            fields: ['product', 'quantity', 'amount']
        }
    },
    created(){
      this.getUser();
    },
    mounted(){
        this.getOrders();
        document.title='Profile';
    },
    methods: {
      getImageSrc(imageData) {
      return `data:image/png;base64,${imageData}`;
    },
    getUser(){
        axios
    .get(`http://127.0.0.1:5000/user/profile?user_id=${localStorage.getItem('user_id')}`,{
        headers: {
            Authorization: localStorage.getItem('token')
        },
    })
    .then((response) => {
      this.user = response.data;
    })
    .catch((error) => console.error('error:', error));
  },
    getOrders(){
    axios
    .get(`http://127.0.0.1:5000/checkout?user_id=${localStorage.getItem('user_id')}`,{
        headers: {
            Authorization: localStorage.getItem('token')
        },
    })
    .then((response) => {
      this.orders = response.data.orders;
    })
    .catch((error) => console.error('error:', error));
  },
  calculateTotalAmount(order) {
        return order.reduce((total, product) => total + product.amount, 0).toFixed(2);
        },

      ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      }
    }
}
</script>

<style scoped>


.search-button {
  border-radius: 20px;
  margin-left: 10px;
  background-color: #007bff;
  color: white;
  font-weight: bold;
}


.login-button {
  border-radius: 20px;
  background-color: #f55;
  color: white;
  font-weight: bold;
}

.nav-item a{
  color: white;
  text-decoration: none;
}

.categories-container {
  padding: 0;
  background-image: url("@/assets/dark.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
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

.user-info {
  text-align: center;
  margin-bottom: 20px;
}

.user-info h2 {
  font-size: 32px;
  font-weight: bold;
}

.user-tickets-heading {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  text-align: center;
}

/* Ticket card styles */
.tickets-list {
  padding: 0 50px 0 50px;
  display: flex;
  flex-wrap: wrap;
  /* justify-content: space-between; */
  margin: 0 -10px;
}

.ticket-card {
  width: 300px;
  display: flex;
  align-items: center; 
  margin: 15px;
  padding: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 15px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.ticket-card:hover {
  transform: translateY(-5px);
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
}
.ticket-image {
  width: 100%; 
  height: 200px; 
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-preview{
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.ticket-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #007bff;
}

.ticket-info {
  font-size: 16px;
  color: #333;
}

.ticket-card b-card-title {
  font-size: 20px;
  font-weight: bold;
}

.ticket-card b-card-text {
  font-size: 16px;
}

.ticket-details {
  flex: 1;
}

/* Media queries for responsiveness */
@media screen and (max-width: 767px) {
  .ticket-card {
    width: 90%;
  }
}

.orders-container {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .order-card {
    margin-bottom: 20px;
  }
  
  .order-table {
    margin-top: 10px;
  }
  .total-amount {
  font-weight: bold;
  margin-top: 10px; /* Adjust as needed for spacing */
}

</style>