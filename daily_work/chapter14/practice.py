# 1. 初始化函数的作用是什么,有什么特点
# 2. 什么是绑定方法,有什么特点
# 3. 对象与类的属性查找顺序什么怎么样的
# 4. 什么是类 什么是对象（复习）
# 5. 程序设计：简易王者荣耀
#     1. 设计王者荣耀中的英雄类,每个英雄对象可以对其他英雄对象使用技能
#     2. 英雄具备以下属性英雄名称,等级,血量和Q_hurt,W_hurt,E_hurt 三个伤害属性,表示各技能的伤害量
#     3.  具备以下技能Q W E三个技能都需要一个敌方英雄作为参数,当敌方血量小于等于0时输出角色死亡


class Hero:
    def __init__(self,name,level,health_points,Q_hurt,W_hurt,E_hurt):
        self._name = name
        self._level = level
        self._health_points = health_points
        self._Q_hurt = Q_hurt
        self._W_hurt = W_hurt
        self._E_hurt = E_hurt

    def get_name(self):
        return self._name

    def Q_attack(self,enemy):
        print('%s Q了 %s 一下'%(self.get_name(),enemy.get_name()))
        enemy.get_attack(self._Q_hurt)

    def W_attack(self, enemy):
        print('%s W了 %s 一下' % (self.get_name(), enemy.get_name()))
        enemy.get_attack(self._W_hurt)

    def E_attack(self, enemy):
        print('%s E了 %s 一下' % (self.get_name(), enemy.get_name()))
        enemy.get_attack(self._E_hurt)

    def get_attack(self,attack_points):
        self._health_points -= attack_points
        if self._health_points > 0:
            print('%s还有%d生命值'%(self.get_name(),self._health_points))
        else:
            print('%s死了'% self.get_name())


if __name__ =='__main__':
    a = Hero('gailun', 10, 100, 15,2,35)
    b = Hero('vn',1, 25, 15, 12, 12)
    a.Q_attack(b)
    a.W_attack(b)
    a.E_attack(b)
