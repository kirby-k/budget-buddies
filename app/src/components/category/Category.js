import React from 'react';
import './category.css';

function Category(props) {
  return (
    <div className='category-tile'>
      <div className='category-icon'>
        {props.img}
      </div>
      <div className='category-text'>
        {props.text}
      </div>
    </div>
  );
}
export default Category;