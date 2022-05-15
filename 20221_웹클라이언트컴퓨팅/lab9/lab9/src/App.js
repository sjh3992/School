import React, { useState } from 'react';
import NewsList from './components/NewsList';
import Categories from './components/Categories';
import TextBox from './components/Text';

let flag = false;

const App = () => {
  const [category, setCategory] = useState('all');
  const onSelect = category => setCategory(category);

  return (
  <>
    <Categories category={category} onSelect={onSelect}/>
    <TextBox />
    <NewsList category={category}/>
  </>
  );
};

export default App;
