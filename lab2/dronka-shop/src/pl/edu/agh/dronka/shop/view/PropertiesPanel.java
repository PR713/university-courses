package pl.edu.agh.dronka.shop.view;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

import javax.swing.BoxLayout;
import javax.swing.JCheckBox;
import javax.swing.JPanel;

import pl.edu.agh.dronka.shop.controller.ShopController;
import pl.edu.agh.dronka.shop.model.Category;
import pl.edu.agh.dronka.shop.model.filter.ItemFilter;

public class PropertiesPanel extends JPanel {

	private static final long serialVersionUID = -2804446079853846996L;
	private ShopController shopController;

	private ItemFilter filter = new ItemFilter();

	public PropertiesPanel(ShopController shopController) {
		this.shopController = shopController;
		setLayout(new BoxLayout(this, BoxLayout.PAGE_AXIS));
	}

	private void addListener(String property_name) {
		add(createPropertyCheckbox(property_name, new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent event) {
				boolean selected = ((JCheckBox) event.getSource()).isSelected();
				if (selected) {
					if (filter.getItemSpec().getDetails() == null) {
						Map<String, Object> map = new HashMap<>();
						map.put(property_name, selected);
						filter.getItemSpec().setDetails(map);
					} else {
						filter.getItemSpec().getDetails().put(property_name, selected);
					}
				} else {
					filter.getItemSpec().getDetails().remove(property_name); //usuwa ze wzorca filtrowania ten detail
				}
				shopController.filterItems(filter);
			}
		}));
	}


	public void fillProperties() {
		removeAll();

		Category category = shopController.getCurrentCategory();
		filter.getItemSpec().setCategory(category);
		add(createPropertyCheckbox("Tanie bo polskie", new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent event) {
				filter.getItemSpec().setPolish(
						((JCheckBox) event.getSource()).isSelected());
				shopController.filterItems(filter);
			}
		}));

		add(createPropertyCheckbox("Używany", new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent event) {
				filter.getItemSpec().setSecondhand(
						((JCheckBox) event.getSource()).isSelected());
				shopController.filterItems(filter);
			}
		}));

		switch(category) {
			case BOOKS: {
				addListener("Twarda oprawa");
				break;
			}
			case ELECTRONICS: {
				addListener("Gwarancja");
				addListener("Mobilny");
				break;
			}
			case MUSIC: {
				addListener("Dołączone video");
				break;
			}
			case SPORT,FOOD: {
				break;
			}

		}




	}

	private JCheckBox createPropertyCheckbox(String propertyName,
			ActionListener actionListener) {

		JCheckBox checkBox = new JCheckBox(propertyName);
		checkBox.setSelected(false);
		checkBox.addActionListener(actionListener);

		return checkBox;
	}

}
