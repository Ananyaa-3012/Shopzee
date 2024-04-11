<template>
  <div>
    <img alt="Shopzee Logo" src="../assets/shopzee.jpg" class="logo" style="width: 210px; height: 167px;border-radius: 30px;">    
    <b-form @submit="onSubmit" @reset="onReset" v-if="show" class="register">
      <br>
        <h3>Store Manager Login</h3>
      
      <b-form-group id="input-group-2" label="Your Email:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.email"
          placeholder="Enter Email"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
        <b-form-input
          type="password"
          id="input-2"
          v-model="form.password"
          placeholder="Enter password"
          required
        ></b-form-input>
      </b-form-group>

      <br><br>
      

      <b-button type="submit" variant="primary">Submit</b-button>
      <br><br>
      <b-button type="reset" variant="danger">Reset</b-button>
      <br><br>
      <p class="signup-link">Don't have an account? <router-link to="/store/register">Create one</router-link></p>
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
    created(){document.title='Store Manager Login';},
    methods: {
        ...mapActions({
            login: 'StoreLOGIN_ACTION'
        }),
        
      onSubmit(event) {
        event.preventDefault()
        let payload = {"email":this.form.email,"password":this.form.password}
        console.log(payload)
        this.login(payload)
        .then(() => {
          // Reset form after successful signup
          this.onReset(event);
          // Show success message or redirect if needed
        })
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
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
.register input{
    width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-right: auto;
    margin-left: auto;
    border: 3px solid skyblue;
}

.register button{
    width: 320px;
    height: 40px;
    border: 3px solid black;
    background: skyblue;
    color: black;
    cursor: pointer;
}
</style>
