#ifndef PRINT_HPP_
#define PRINT_HPP_
#include <iostream>

template <typename Collection>
void print(const Collection& coll)
{
  for (const auto& c: coll) 
    std::cout << c << std::endl;
}












#endif //PRINT_HPP_
