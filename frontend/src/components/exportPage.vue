<template>
    <div>
        <b-navbar toggleable="lg" type="danger" variant="info" class="gradient-nav">
      <b-navbar-brand  class="navbar-logo"><router-link to="/store/category">Shopzee</router-link></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          
          <b-button variant="secondary" class="login-button" @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Export Data</h5>
                <p class="card-text">Export your data in CSV format</p>
            </div>
        </div>
        <div id="divToPrint" class="mt-5">
            <h4>Product Details</h4>
            <div class="table-responsive">
                <table class="table table-bordered" >
                    <!-- @click="printDocument()" -->
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Category</th>
                            <th>Stock Remaining</th>
                            <th>Manufacturing Date</th>
                            <th>Expiry Date</th>
                            <th>Price</th>
                            <th>Units Sold</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="product in products" :key="product.id">
                            <td>{{ product?.name }}</td>
                            <td>{{ product?.category }}</td>
                            <td>{{ product?.stock }}</td>
                            <td>{{ product?.manufac }}</td>
                            <td>{{ product?.expiry }}</td>
                            <td>{{ product?.price }}</td>
                            <td>{{ product?.total_sales }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="mt-5 text-center">
            <button class="btn btn-primary" @click="exportData">Download as CSV file</button>
        </div>

        
    </div>
</template>

<script>
import axios from 'axios'
import {mapActions} from 'vuex'


export default {
    
    data() {
        return {
            products: []
        }
    },
    mounted(){
        this.getProducts();
        document.title='Export Data'
    },
    methods: {
        getProducts(){
            const apiurl = `http://127.0.0.1:5000/export` 
            axios.get(apiurl,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.products=response.data;
                console.log(this.products)
            })
          .catch(error=> console.error('error :',error));

        },
        exportData() {
            const csvContent = this.convertDataToCSV(this.products);
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const dataURI = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = dataURI;
            link.download = 'products_data.csv';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
         },
         convertDataToCSV(data) {
            const header = 'Product,Category,Stock_Remaining,Manufacturing_Date,Expiry_Date,Price,Units_Sold\n';
            const csvRows = data.map(product => `${product.name},${product.category},${product.stock},${product.manufac},${product.expiry},${product.price},${product.total_sales}`).join('\n');
            return header + csvRows;
        },
        ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
        logout(){
        this.signOut()
      },

    },
}
</script>

<style scoped>

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
}</style>