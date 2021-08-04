import React from 'react'
import Category from '../components/category/Category';
import HomeIcon from '@material-ui/icons/Home';
import './createBudget.css'

export const CreateBudget = () => {
  return (
    <div className='category-container'>
      <div className='test'>
        <Category
          img={<HomeIcon style={{ fontSize: 50 }} />}
          text={'Housing'} />
      </div>
      <div className='test'>
        <Category
          img={<HomeIcon style={{ fontSize: 50 }} />}
          text={'Housing'} />
      </div>
      <div className='test'>
        <Category
          img={<HomeIcon style={{ fontSize: 50 }} />}
          text={'Housing'} />
      </div>
    </div>
  );
}

export default CreateBudget