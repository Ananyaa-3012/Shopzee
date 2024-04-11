<template>
  <div>
    <img alt="Shopzee Logo" src="../assets/shopzee.jpg" class="logo" style="width: 210px; height: 167px;border-radius: 30px;">    
    <b-form @submit="onSubmit" @reset="onReset" v-if="show" class="login-form">
      <br>
      <h3>Store Manager Register</h3>

      <b-form-group label="Your Name:" label-for="input-name">
        <b-form-input
          id="input-name"
          v-model="form.name"
          placeholder="Enter name"
          required
          class="login-input"
        ></b-form-input>
      </b-form-group>
      
      <b-form-group label="Your Email" label-for="input-email">
        <b-form-input
          id="input-email"
          v-model="form.email"
          placeholder="Enter email"
          type="email"
          required
          class="login-input"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Your Password:" label-for="input-password">
        <b-form-input
          id="input-password"
          v-model="form.password"
          placeholder="Enter password"
          type="password"
          required
          class="login-input"
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary" class="login-btn">Submit</b-button>      
      <br><br>

      <p class="signup-link">Already have an account? <router-link to="/store/login">Login here</router-link></p>
      <p class="signup-link">Not a Store Manager? <router-link to="/">Click here</router-link></p>
    </b-form>
  </div>
</template>






<script>

import {mapActions} from 'vuex'

export default {
    data() {
      return {
        form: {
          email: '',
          password:'',
          
        },
        show: true
      }
    },
    created(){document.title='Store Manager Register';},
    methods: {
      ...mapActions({
        signUp: 'StoreSIGNUP_ACTION'
      }),
      onSubmit(event) {
        event.preventDefault()
        let payload = {"name" : this.form.name,"email":this.form.email, "password":this.form.password}
        console.log(payload)
        this.signUp(payload)
        
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.email = ''
        this.form.password=''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }


</script>



<style scoped>
.login-form input{
    width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-right: auto;
    margin-left: auto;
    border: 3px solid skyblue;
}

.login-form button{
    width: 320px;
    height: 40px;
    border: 3px solid black;
    background: skyblue;
    color: black;
    cursor: pointer;
}
</style>