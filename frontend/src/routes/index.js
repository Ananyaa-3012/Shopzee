import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from '../view/LandingPage.vue'
import LoginView from '../view/LoginView.vue'
import SignUpView from '../view/SignUpView.vue'
import StoreSignUpView from '../view/StoreSignUpView.vue'
import homePageView from '../view/homePageView.vue'
import storeLogin from '../components/storeLogin.vue'
import userProduct from '../components/userProduct.vue'
import createCategory  from '../components/createCategory.vue'
import storeCat from '../components/storeCat.vue'
import editCategory from '../components/editCategory.vue'
import storeProduct from '../components/storeProduct.vue'
import createProduct from '../components/createProduct.vue'
import editProduct from '../components/editProduct.vue'
import addCart from '../components/addCart.vue'
import userCart from '../components/userCart.vue'
import updateCart from '../components/updateCart.vue'
import userOrders from '../components/userOrders.vue'
import adminLogin from '../components/adminLogin.vue'
import adminDashboard from '../components/adminDashboard.vue'
import adminCategory from '../components/adminCategory.vue'
import storeApproval from '../components/storeApproval.vue'
import categoryApproval from '../components/categoryApproval.vue'
import categorySearch from '../components/categorySearch.vue'
import productSearch from '../components/productSearch.vue'
import userProfile from '../components/userProfile.vue'
import exportPage from '../components/exportPage.vue'
import jwt_decode from 'jwt-decode'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'LandingPage',
        component: LandingPage,
    },

    //User Routes
    {
        path: '/register',
        name: 'SignUp',
        component: SignUpView,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView
    },
    {
        path: '/home',
        name: 'home',
        component: homePageView,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },
    {
        
        path: '/products/:cat_id',
        name: 'products',
        component: userProduct,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },
    {
        path: '/cart/add/:pdt_id',
        name: 'addCart',
        component: addCart,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },
    {
        path: '/cart',
        name: 'cartView',
        component: userCart,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },
    {
        path: '/cart/edit/:pdt_id',
        name: 'updateCart',
        component: updateCart,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },
    {
        path: '/orders',
        name: 'userOrders',
        component: userOrders,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },
    {
        path: '/search/:keyword',
        name: 'categorySearch',
        component: categorySearch,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },
    {
        path: '/search/:cat_id/:keyword',
        name: 'productSearch',
        component: productSearch,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },
    {
        path: '/user/profile',
        name: 'userProfile',
        component: userProfile,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: false }
    },

    
    //Store Routes
    {
        path: '/store/register',
        name: 'StoreSignUp',
        component: StoreSignUpView,
    },
    {
        path: '/store/login',
        name: 'storeLogin',
        component: storeLogin,
    },
    {
        path: '/store/products/:cat_id',
        name: 'storeProducts',
        component: storeProduct,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: true }
    },
    {
        path: '/cat_create',
        name: 'createCategory',
        component: createCategory,
        meta: { requiresAuth: true, notUser: true }
    },
    {
        path: '/store/category',
        name: 'storeCat',
        component: storeCat,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: true }
    },
    {
        path: '/pdt_create/:cat_id',
        name: 'createProduct',
        component: createProduct,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: true }
    },
    {
        path: '/pdt_update/:cat_id/:pdt_id',
        name: 'editProduct',
        component: editProduct,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: true }
    },
    {
        path: '/cat_update/:cat_id',
        name: 'editCategory',
        component: editCategory,
        meta: { requiresAuth: true, notUser: true }
    },
    {
        path: '/export',
        name: 'exportData',
        component: exportPage,
        meta: { requiresAuth: true, requiresAdmin: false, requiresStore: true }
    },

    //Admin Routes

    {
        path: '/admin/login',
        name: 'adminLogin',
        component: adminLogin
    },
    {
        path: '/admin/dashboard',
        name: 'adminDashboard',
        component: adminDashboard,
        meta: { requiresAuth: true, requiresAdmin: true, requiresStore: false }
    },
    {
        path: '/admin/category',
        name: 'adminCategory',
        component: adminCategory,
        meta: { requiresAuth: true, requiresAdmin: true, requiresStore: false }
    },
    {
        path: '/approval/managers',
        name: 'storeApproval',
        component: storeApproval,
        meta: { requiresAuth: true, requiresAdmin: true, requiresStore: false }
    },
    {
        path: '/approval/categories',
        name: 'categoryApproval',
        component: categoryApproval,
        meta: { requiresAuth: true, requiresAdmin: true, requiresStore: false }
    }

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })



function verifyToken(token){
    try{
        const decoded = jwt_decode(token)
        console.log(decoded)
        return decoded
    }catch(error){
        console.error(error)
        return null
    }
}

router.beforeEach((to, from, next)=> {
    const isAuthenticated = localStorage.getItem('token')
    const isAdmin = localStorage.getItem('user_type') === 'admin'
    const isStore = localStorage.getItem('user_type') === 'storeManager'
    const isUser = localStorage.getItem('user_type') === 'user'

    if(to.matched.some(record => record.meta.requiresAuth)){
        if(isAuthenticated === 'null'){
            alert('Please Login to continue')
            next({path: '/'})
        }else{
            try{
                const decodedToken = verifyToken(isAuthenticated)
                if(decodedToken && decodedToken.exp * 1000 > Date.now()){
                    if(to.matched.some(record => record.meta.requiresAdmin)&& !isAdmin){
                        alert('Only Admins can access');
                        localStorage.setItem('token','null');
                        localStorage.setItem('user_type','null');
                        next({path: '/'})
                    }else if(to.matched.some(record => record.meta.requiresStore)&& !isStore){
                        alert('Only Store Managers can access');
                        localStorage.setItem('token','null');
                        localStorage.setItem('user_type','null');
                        next({path: '/'})
                    }else if(to.matched.some(record => record.meta.notUser)&& isUser){
                        alert('Users cannot access');
                        localStorage.setItem('token','null');
                        localStorage.setItem('user_type','null');
                        next({path: '/'})
                    }else{
                        next()
                    }
                }else{
                    alert('Session expired!!')
                    next({path: '/'})
                }
            }catch(error){
                console.error(error)
                next({path: '/'})
            }
        }
    }else{
        next()
    }
})

export default router;

